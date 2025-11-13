````markdown
# Quick Start Guide

## Project Overview

Your Stock Analyzer now has:
- ✅ **Modern fintech frontend** (`stock-analyzer.html`)
- ✅ **Production-ready FastAPI backend** with modular architecture
- ✅ **Real-time stock data** from Yahoo Finance
- ✅ **AI-powered insights** from Google Gemini
- ✅ **Comprehensive error handling** and fallback mock data

## Accessing the Application

### Frontend
- **Modern UI:** http://127.0.0.1:8000/static/stock-analyzer.html
- **Original UI:** http://127.0.0.1:8000/static/index.html

### Backend API
- **Interactive Docs:** http://127.0.0.1:8000/docs (Swagger UI)
- **Alternative Docs:** http://127.0.0.1:8000/redoc (ReDoc)
- **Root Endpoint:** http://127.0.0.1:8000/

## Testing the API

### Using Browser
1. Go to http://127.0.0.1:8000/docs
2. Click on `/analyze` endpoint
3. Enter ticker: `AAPL`
4. Click "Try it out"

### Using cURL
```bash
# Get stock price with AI analysis
curl "http://127.0.0.1:8000/analyze?ticker=AAPL"

# Get just the price (faster)
curl "http://127.0.0.1:8000/price?ticker=GOOGL"

# Check API health
curl "http://127.0.0.1:8000/health"
```

### Using Python
```python
import requests

# Analyze a stock
response = requests.get("http://127.0.0.1:8000/analyze?ticker=MSFT")
data = response.json()
print(f"{data['ticker']}: ${data['price']} ({data['change']})")
print(f"Insight: {data['ai_insight']}")
```

### Using JavaScript
```javascript
// In browser console or frontend
fetch("http://127.0.0.1:8000/analyze?ticker=TSLA")
  .then(r => r.json())
  .then(data => {
    console.log(`${data.ticker}: $${data.price}`);
    console.log(`AI Insight: ${data.ai_insight}`);
  })
  .catch(err => console.error("Error:", err));
```

## Backend Structure

```
backend/
├── main.py                    # All API endpoints
├── utils/
│   ├── stock_fetcher.py      # Fetch stock data from Yahoo Finance
│   └── ai_generator.py       # Generate insights from Gemini API
├── requirements.txt          # Python dependencies
├── .env                      # Your API keys (don't commit!)
└── README.md                 # Full documentation
```

## API Endpoints Summary

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/analyze?ticker=AAPL` | GET | Get price + AI insight |
| `/price?ticker=AAPL` | GET | Get price only (faster) |
| `/health` | GET | Check API status |
| `/models` | GET | List AI models |
| `/` | GET | API info |

## Example Response

```json
{
  "ticker": "AAPL",
  "price": 192.50,
  "change": "+2.45%",
  "ai_insight": "Apple shows stable upward trend with strong ecosystem integration...",
  "currency": "USD",
  "company_name": "Apple Inc.",
  "data_source": "Yahoo Finance"
}
```

## Configuration

### Set Your Gemini API Key

1. Get key from https://ai.google.dev
2. Open `.env` file
3. Add: `GEMINI_API_KEY=your_key_here`
4. Save and restart server

Without the key, the app uses mock data—still fully functional!

## Supported Stocks

Works with any valid stock ticker:
- Tech: AAPL, GOOGL, MSFT, NVDA, META
- Automotive: TSLA
- Retail: AMZN, WMT
- Finance: JPM, GS
- Healthcare: JNJ, PFE

And thousands more!

## What's New in v2.0

✅ Modular architecture (separate utils modules)
✅ Better error handling with detailed messages
✅ Enhanced API documentation
✅ Mock data fallback when APIs unavailable
✅ Health check endpoint
✅ Support for both real and mock data sources
✅ Query parameter validation with FastAPI

## Troubleshooting

**Frontend not loading?**
- Make sure server is running: `uvicorn main:app --reload`
- Try: http://127.0.0.1:8000/static/stock-analyzer.html

**API returning mock data?**
- This is normal if API key isn't set or yfinance is rate-limited
- Set `GEMINI_API_KEY` in .env for real AI insights

**Getting CORS errors?**
- CORS is enabled for all origins—this shouldn't happen
- Check your frontend URL matches the request

**Server won't start?**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.10+)

## Next Steps

1. ✅ Test the frontend at http://127.0.0.1:8000/static/stock-analyzer.html
2. ✅ Try the API at http://127.0.0.1:8000/docs
3. ✅ Set your Gemini API key in .env for real AI insights
4. ✅ Customize the mock data in `utils/stock_fetcher.py` if needed
5. ✅ Deploy to production when ready

Enjoy your Stock Analyzer! 📈

````
