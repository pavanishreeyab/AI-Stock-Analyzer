from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Import utility functions
from utils.stock_fetcher import fetch_stock_data, format_change
from utils.ai_generator import generate_ai_insight, validate_api_key

# Load environment variables
load_dotenv()

# Configure Gemini API key if available
gemini_key = os.getenv("GEMINI_API_KEY")
if gemini_key:
    genai.configure(api_key=gemini_key)

# Create FastAPI app
app = FastAPI(
    title="Stock Analyzer API",
    description="Real-time stock analysis with AI-powered insights",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for frontend
app.mount("/static", StaticFiles(directory="../frontend"), name="static")


# ============ API Endpoints ============

@app.get("/")
def home():
    """Root endpoint - API status check"""
    return {
        "message": "Stock Analyzer API is running!",
        "version": "2.0.0",
        "endpoints": {
            "analyze": "/analyze?ticker=AAPL",
            "docs": "/docs"
        }
    }


@app.get("/analyze")
def analyze_stock(ticker: str = Query(..., min_length=1, max_length=10, description="Stock ticker symbol (e.g., AAPL)")):
    """
    Analyze a stock with current price and AI-generated insight.
    
    Query Parameters:
        ticker (str): Stock ticker symbol (required, 1-10 characters)
    
    Returns:
        JSON with ticker, price, change, and AI insight
    
    Example:
        GET /analyze?ticker=AAPL
    """
    try:
        # Validate ticker
        ticker = ticker.upper().strip()
        if not ticker or not ticker.isalpha():
            raise HTTPException(
                status_code=400,
                detail="Invalid ticker. Must be 1-10 alphabetic characters (e.g., AAPL)"
            )
        
        # Fetch stock data
        stock_data = fetch_stock_data(ticker)
        price = stock_data["price"]
        change = stock_data["change"]
        
        # Generate AI insight
        ai_insight = generate_ai_insight(ticker, price, change)
        
        # Format response
        return {
            "ticker": ticker,
            "price": round(price, 2),
            "change": format_change(change),
            "ai_insight": ai_insight,
            "currency": stock_data.get("currency", "USD"),
            "company_name": stock_data.get("name", ticker),
            "data_source": stock_data.get("source", "Unknown")
        }
    
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


@app.get("/price")
def get_stock_price(ticker: str = Query(..., min_length=1, max_length=10, description="Stock ticker symbol")):
    """
    Get current stock price without AI analysis.
    
    Query Parameters:
        ticker (str): Stock ticker symbol (required)
    
    Returns:
        JSON with ticker, price, and change percentage
    
    Example:
        GET /price?ticker=GOOGL
    """
    try:
        ticker = ticker.upper().strip()
        if not ticker or not ticker.isalpha():
            raise HTTPException(
                status_code=400,
                detail="Invalid ticker format"
            )
        
        stock_data = fetch_stock_data(ticker)
        
        return {
            "ticker": ticker,
            "price": round(stock_data["price"], 2),
            "change": format_change(stock_data["change"]),
            "currency": stock_data.get("currency", "USD"),
            "company_name": stock_data.get("name", ticker)
        }
    
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "api_version": "2.0.0",
        "ai_api_available": validate_api_key()
    }


@app.get("/models")
def list_models():
    """List available AI models (requires Gemini API key)"""
    try:
        if not validate_api_key():
            return {
                "message": "Gemini API key not configured",
                "models": []
            }
        
        models = genai.list_models()
        return {
            "available_models": [m.name for m in models],
            "total": len(list(models))
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
