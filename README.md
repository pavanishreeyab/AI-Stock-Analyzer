# AI Stock Analyzer

A modern, full-stack stock analysis application built with FastAPI and vanilla JavaScript. Get real-time stock prices and AI-powered investment insights powered by Google Gemini.

## Features

✨ **Real-Time Stock Data** - Fetch live stock prices from Yahoo Finance  
🤖 **AI-Generated Insights** - Get investment recommendations using Google Gemini  
💎 **Modern UI** - Dark theme with fintech aesthetic and smooth animations  
🔄 **Fallback System** - Works offline with mock data when APIs unavailable  
📊 **Market Analysis** - View market cap, volume, P/E ratio, and dividend yield  
🎯 **Fast & Reliable** - Async FastAPI backend with comprehensive error handling  
📱 **Responsive Design** - Works seamlessly on desktop and mobile devices  

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js (optional, not required for this project)
- Git

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/AI-Stock-Analyzer.git
cd AI-Stock-Analyzer
```

2. **Set Up Backend**
```bash
cd backend
pip install -r requirements.txt
```

3. **Configure Environment (Optional)**
Create a `.env` file in the `backend/` folder to enable Google Gemini AI insights:
```
GEMINI_API_KEY=your_api_key_here
```

To get a Gemini API key:
- Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- Create a new API key
- Paste it into your `.env` file

Without the API key, the app uses pre-written insights and works perfectly fine.

### Running the Application

**Start Backend Server:**
```bash
cd backend
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Access Frontend:**
- Open `frontend/index.html` directly in your browser, OR
- Navigate to `http://127.0.0.1:8000` if backend is running

## Project Structure

```
AI-Stock-Analyzer/
├── backend/                          # FastAPI backend application
│   ├── main.py                      # Main FastAPI app with 5 endpoints
│   ├── requirements.txt             # Python dependencies
│   └── utils/                       # Utility modules
│       ├── __init__.py
│       ├── stock_fetcher.py        # Stock data fetching & fallback logic
│       └── ai_generator.py         # AI insight generation with Gemini API
│
├── frontend/                         # Frontend application
│   ├── index.html                  # Main HTML document
│   ├── style.css                   # Styling (dark theme, animations)
│   └── script.js                   # JavaScript logic & mock database
│
├── docs/                            # Documentation
│   ├── README.md                   # Full technical documentation
│   ├── QUICKSTART.md               # Quick reference guide
│   ├── DEPLOYMENT.md               # Production deployment options
│   ├── BACKEND_IMPLEMENTATION.md   # Architecture & design details
│   └── [more documentation files]
│
├── README.md                        # This file
└── .gitignore                       # Git ignore rules
```

## API Endpoints

### GET `/analyze?ticker=AAPL`
Returns stock price + AI-generated insight
```json
{
  "stock_data": {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "price": 195.42,
    "change": 2.34,
    "volume": 52380000
  },
  "ai_insight": "Apple continues to dominate..."
}
```

### GET `/price?ticker=AAPL`
Returns stock price only (faster, ~500ms)
```json
{
  "ticker": "AAPL",
  "price": 195.42,
  "change": 2.34
}
```

### GET `/health`
Health check endpoint
```json
{ "status": "healthy" }
```

### GET `/docs`
Interactive API documentation (Swagger UI)

### GET `/redoc`
ReDoc API documentation

## Supported Stock Tickers

By default, the app includes mock data for these stocks:
- **AAPL** - Apple Inc.
- **GOOGL** - Alphabet Inc.
- **MSFT** - Microsoft Corporation
- **TSLA** - Tesla Inc.
- **AMZN** - Amazon Inc.

Any other ticker will attempt to fetch from Yahoo Finance if backend is running.

## Backend Features

### Error Handling
- **Real API Failure** → Automatic fallback to mock data
- **Invalid Ticker** → Clear error message with HTTP 400/422 status
- **Network Issues** → Frontend gracefully falls back to mock data
- **Missing API Key** → Uses pre-written insights instead of Gemini

### Dependencies
- **FastAPI 0.109.0** - Web framework
- **Uvicorn 0.27.0** - ASGI server
- **yfinance 0.2.33** - Yahoo Finance data fetching
- **google-generativeai 0.3.1** - Gemini API integration
- **python-dotenv 1.0.0** - Environment configuration
- **requests 2.31.0** - HTTP client
- **CORS** - Enabled for all origins

## Frontend Features

### Technology Stack
- Vanilla HTML5 / CSS3 / JavaScript (no frameworks)
- Responsive design with CSS Grid & Flexbox
- Smooth animations and transitions
- Dark theme with teal/blue gradient accents

### Mock Database
Built-in mock data for 5 stocks with realistic prices and AI insights. Enables offline testing without backend or API access.

## Configuration

### Backend Configuration

**Change API Port:**
Edit `backend/main.py` and modify the Uvicorn startup command.

**Add Your Own Stocks:**
Edit `backend/utils/stock_fetcher.py` and add entries to `MOCK_STOCKS` dictionary.

**Configure Gemini API:**
1. Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create `.env` file in `backend/` folder:
   ```
   GEMINI_API_KEY=your_key_here
   ```
3. Restart backend server

### Frontend Configuration

**Change Backend URL:**
Edit `frontend/script.js` line 97:
```javascript
const response = await fetch(`http://YOUR_BACKEND_URL/analyze?ticker=${ticker}`);
```

**Add More Stocks to Mock Database:**
Edit `frontend/script.js` and add entries to `stockDatabase` and `insightsDatabase` objects.

## Deployment

### Development
```bash
cd backend
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Production

For production deployment options including Docker, Railway, AWS, Heroku, and more, see [DEPLOYMENT.md](docs/DEPLOYMENT.md)

**Quick Docker Deploy:**
```bash
docker build -t stock-analyzer .
docker run -p 8000:8000 stock-analyzer
```

## Testing

### Manual Testing

1. **Via Frontend UI:**
   - Open `http://127.0.0.1:8000` in browser
   - Enter a ticker (AAPL, GOOGL, MSFT, TSLA, AMZN)
   - Click "Analyze Stock"

2. **Via Swagger UI:**
   - Visit `http://127.0.0.1:8000/docs`
   - Try `/analyze?ticker=AAPL`
   - Try `/price?ticker=AAPL`

3. **Via Command Line:**
   ```bash
   curl "http://127.0.0.1:8000/analyze?ticker=AAPL"
   curl "http://127.0.0.1:8000/price?ticker=GOOGL"
   ```

## Troubleshooting

### "Cannot GET /"
- Ensure backend server is running: `python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000`
- Check port 8000 is available (no other service using it)

### "Failed to fetch from /analyze"
- This is expected! The app will gracefully fall back to mock data
- Mock data is always available for AAPL, GOOGL, MSFT, TSLA, AMZN
- Check browser console for error details

### Stock data not updating
- Ensure `yfinance` is installed: `pip install yfinance`
- Check internet connection (for real stock data fetching)
- Try a different ticker

### Gemini AI insights not showing
- Verify `GEMINI_API_KEY` is set in `.env` file
- Restart backend server after adding API key
- Without the key, pre-written insights are used (completely fine)

## Documentation

Detailed documentation is available in the `docs/` folder:

- **[README.md](docs/README.md)** - Full technical documentation
- **[QUICKSTART.md](docs/QUICKSTART.md)** - Quick reference & examples
- **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Production deployment guide
- **[BACKEND_IMPLEMENTATION.md](docs/BACKEND_IMPLEMENTATION.md)** - Architecture deep-dive
- **[IMPLEMENTATION_SUMMARY.md](docs/IMPLEMENTATION_SUMMARY.md)** - Project overview
- **[COMPLETE_FILE_LISTING.md](docs/COMPLETE_FILE_LISTING.md)** - Every file explained
- **[START_HERE.md](docs/START_HERE.md)** - Visual quick-start guide

## Performance

### Response Times
- **`/price` endpoint:** ~500ms - 1 second (stock data only)
- **`/analyze` endpoint:** ~2-4 seconds (includes AI analysis)
- **Frontend load:** <1 second (no dependencies)

### Scalability
- Async backend handles multiple concurrent requests
- Stateless design allows easy horizontal scaling
- Mock data fallback ensures zero-downtime operation

## Security

### Best Practices Implemented
- ✅ API key stored in `.env` file (not in code)
- ✅ Input validation on all API endpoints
- ✅ CORS configured for proper cross-origin requests
- ✅ Error messages don't leak sensitive information
- ✅ `.gitignore` prevents committing sensitive files

### Important Notes
- Never commit `.env` file to GitHub
- Regenerate API keys if accidentally exposed
- Keep dependencies updated for security patches

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

Built with ❤️ as a demonstration of modern full-stack Python web development with AI integration.

## Support

For questions, issues, or suggestions:
- Create an issue on GitHub
- Check existing documentation in `docs/` folder
- Review API documentation at `/docs` endpoint

## Roadmap

Future enhancements:
- 📈 Historical price charts
- 📊 Portfolio tracking
- 🔔 Price alerts
- 💾 Saved watchlists
- 🌙 User accounts & authentication
- 📱 Mobile app version

---

**Get Started Now:** Run the commands in the [Quick Start](#quick-start) section above!
