````markdown
# Stock Analyzer API - FastAPI Backend

A modern FastAPI backend service for real-time stock analysis with AI-powered insights using Google Gemini.

## Features

✅ **Real-time Stock Data** — Fetch current prices and changes using yfinance
✅ **AI-Powered Insights** — Generate investment summaries using Google Gemini API  
✅ **Mock Data Fallback** — Works even when APIs are unavailable
✅ **Comprehensive Error Handling** — Graceful error messages and fallbacks
✅ **CORS Support** — Accessible from any frontend domain
✅ **Interactive API Docs** — Built-in Swagger UI and ReDoc
✅ **Health Checks** — Monitor API and AI service availability

## Project Structure

```
backend/
├── main.py                 # Main FastAPI application and endpoints
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
├── utils/
│   ├── __init__.py
│   ├── stock_fetcher.py   # Stock data fetching with yfinance
│   └── ai_generator.py    # AI insight generation with Gemini
├── index.html             # Original frontend
├── stock-analyzer.html    # Modern fintech frontend
└── README.md              # This file
```

## Installation

### 1. Clone/Download Project

```bash
cd backend
```

### 2. Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### Setup .env File

Create a `.env` file in the project root:

```env
# Google Gemini API Key (get from https://ai.google.dev)
GEMINI_API_KEY=your_gemini_api_key_here

# Optional: Finnhub API Key (not currently used)
FINNHUB_API_KEY=your_finnhub_api_key_here
```

**Note:** The app works without a Gemini API key—it will use mock data for AI insights.

### Get Gemini API Key

1. Go to [Google AI Studio](https://ai.google.dev)
2. Click "Get API Key"
3. Create a new API key
4. Copy the key to your `.env` file

## Running the Server

### Development Mode (with auto-reload)

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Server runs at: `http://127.0.0.1:8000`

## API Endpoints

### 1. `/analyze?ticker=AAPL`

Analyze a stock with current price and AI-generated insight.

**Method:** `GET`

**Query Parameters:**
- `ticker` (string, required): Stock ticker symbol (1-10 characters, e.g., AAPL)

**Response Example:**
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

**Example Requests:**

```bash
# Using curl
curl "http://127.0.0.1:8000/analyze?ticker=AAPL"

# Using Python requests
import requests
response = requests.get("http://127.0.0.1:8000/analyze?ticker=GOOGL")
print(response.json())

# Using JavaScript fetch
fetch("http://127.0.0.1:8000/analyze?ticker=MSFT")
  .then(r => r.json())
  .then(data => console.log(data))
```

### 2. `/price?ticker=AAPL`

Get current stock price without AI analysis (faster).

**Method:** `GET`

**Query Parameters:**
- `ticker` (string, required): Stock ticker symbol

**Response Example:**
```json
{
  "ticker": "AAPL",
  "price": 192.50,
  "change": "+2.45%",
  "currency": "USD",
  "company_name": "Apple Inc."
}
```

### 3. `/health`

Check API health and service status.

**Method:** `GET`

**Response Example:**
```json
{
  "status": "healthy",
  "api_version": "2.0.0",
  "ai_api_available": true
}
```

### 4. `/models`

List available AI models (requires Gemini API key).

**Method:** `GET`

**Response Example:**
```json
{
  "available_models": [
    "models/gemini-pro",
    "models/gemini-2.5-flash"
  ],
  "total": 2
}
```

### 5. `/`

Root endpoint - API status check.

**Method:** `GET`

**Response Example:**
```json
{
  "message": "Stock Analyzer API is running!",
  "version": "2.0.0",
  "endpoints": {
    "analyze": "/analyze?ticker=AAPL",
    "docs": "/docs"
  }
}
```

## API Documentation

### Interactive Documentation

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## Supported Stock Tickers

The API works with any valid stock ticker. Common examples:

| Ticker | Company |
|--------|---------|
| AAPL   | Apple Inc. |
| GOOGL  | Alphabet Inc. |
| MSFT   | Microsoft Corporation |
| AMZN   | Amazon.com Inc. |
| TSLA   | Tesla Inc. |
| META   | Meta Platforms Inc. |
| NVDA   | NVIDIA Corporation |

## Error Handling

The API provides clear error messages:

### Invalid Ticker

**Request:**
```
GET /analyze?ticker=INVALID123
```

**Response:**
```json
{
  "detail": "Invalid ticker. Must be 1-10 alphabetic characters (e.g., AAPL)"
}
```

### Stock Not Found

**Request:**
```
GET /analyze?ticker=FAKESTOCK
```

**Response:**
```json
{
  "detail": "Stock ticker 'FAKESTOCK' not found and no mock data available"
}
```

### Missing Ticker

**Request:**
```
GET /analyze
```

**Response:**
```json
{
  "detail": "Query parameter 'ticker' is required"
}
```

## Mock Data

When real APIs are unavailable, the backend uses mock data for these stocks:
- AAPL, GOOGL, MSFT, TSLA, AMZN

All requests return realistic sample data and mock AI insights.

## Utility Modules

### `utils/stock_fetcher.py`

Handles stock data fetching with fallback to mock data:

```python
from utils.stock_fetcher import fetch_stock_data, format_change

# Fetch real or mock data
stock = fetch_stock_data("AAPL")
print(stock["price"])  # 187.50
print(stock["change"])  # 1.2

# Format change percentage
formatted = format_change(1.2)  # "+1.20%"
```

### `utils/ai_generator.py`

Generates AI insights using Gemini API with fallback:

```python
from utils.ai_generator import generate_ai_insight, validate_api_key

# Generate insight
insight = generate_ai_insight("AAPL", 187.50, 1.2)

# Check if API is available
is_available = validate_api_key()
```

## Frontend Integration

Connect any frontend to these endpoints:

### Example JavaScript Integration

```javascript
// Analyze stock
async function analyzeStock(ticker) {
  const response = await fetch(`http://127.0.0.1:8000/analyze?ticker=${ticker}`);
  const data = await response.json();
  
  if (!response.ok) {
    console.error("Error:", data.detail);
    return;
  }
  
  console.log(`${data.ticker}: $${data.price} (${data.change})`);
  console.log(`AI Insight: ${data.ai_insight}`);
}

analyzeStock("AAPL");
```

## Deployment

### Local Development
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Production (using Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### Docker (Optional)

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Troubleshooting

### Issue: "No module named 'utils'"
**Solution:** Make sure you're running the server from the `backend/` directory.

### Issue: "Gemini API key not configured"
**Solution:** Set `GEMINI_API_KEY` in your `.env` file or the app will use mock data.

### Issue: "ModuleNotFoundError: No module named 'yfinance'"
**Solution:** Install dependencies: `pip install -r requirements.txt`

### Issue: CORS errors in frontend
**Solution:** The API already has CORS enabled for all origins. Check that your frontend URL matches the request origin.

## Performance Tips

- Use `/price` instead of `/analyze` if you don't need AI insights (faster)
- Cache responses on the frontend for frequently accessed stocks
- Use the health endpoint to monitor API availability

## Future Enhancements

- [ ] Add database caching
- [ ] Implement rate limiting
- [ ] Add WebSocket support for real-time updates
- [ ] Support multiple AI models
- [ ] Add technical analysis indicators
- [ ] Historical data endpoints

## License

MIT License - feel free to use this project

## Support

For issues or questions, check the interactive documentation at `/docs`

````
