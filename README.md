# 📊 AI Stock Analyzer - Complete End-to-End Web Application

A modern, full-stack stock analysis web application combining real-time stock data with AI-powered investment insights. Features advanced analysis including sentiment indicators, stock comparison, and regenerable AI insights.

## 🎯 Project Overview

AI Stock Analyzer is a complete single-page web application that enables users to:

- **Analyze Stocks**: Enter stock ticker to get real-time price and AI-generated insights
- **Compare Stocks**: View two stocks side-by-side with sentiment indicators
- **Regenerate Insights**: Get fresh AI perspectives with alternative analysis angles
- **Sentiment Analysis**: Visual indicators (📈 bullish, 📉 bearish, ⚖️ neutral)
- **Comprehensive Stats**: Market cap, 52-week high, volume, and P/E ratios

## 🛠️ Tech Stack

### Frontend
- **HTML5, CSS3, Vanilla JavaScript** - No frameworks, pure ES6+
- **Design**: Dark mode fintech theme with teal/blue gradients
- **Fonts**: Poppins (headings), Inter (body)
- **Responsive**: Mobile-first design with animations

### Backend
- **FastAPI** - Modern Python async web framework
- **Uvicorn** - ASGI production server
- **Google Gemini API** - AI-powered investment analysis
- **yfinance** - Real-time stock data
- **python-dotenv** - Environment configuration

### APIs
- **Gemini API** - Investment insights and analysis
- **Yahoo Finance (yfinance)** - Stock price data
- **Finnhub API** (optional) - Alternative data source

## 📁 Project Structure

```
AI-Stock-Analyzer/
├── backend/
│   ├── main.py                 # 7 FastAPI endpoints
│   ├── utils/
│   │   ├── stock_fetcher.py   # Stock data + mock fallback
│   │   └── ai_generator.py    # Gemini API + sentiment classification
│   ├── requirements.txt
│   └── .env                    # API keys (not in repo)
│
├── frontend/
│   └── index.html              # Single-file SPA (850+ lines)
│
├── README.md                   # This file
├── .gitignore
└── docs/                       # Additional documentation
```

## 🚀 Quick Start

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GEMINI_API_KEY=your_key_here" > .env

# Run server
uvicorn main:app --reload --port 8000
```

### Frontend Access

Open in browser: `http://127.0.0.1:8000/static/index.html`

Or access with Swagger docs: `http://127.0.0.1:8000/docs`

## 📡 API Endpoints (7 Total)

### 1. **Analyze Stock**
```
GET /analyze?ticker=AAPL
```
Returns price, change, AI insight, and sentiment indicator.

### 2. **Get Price**
```
GET /price?ticker=AAPL
```
Quick price check without AI analysis.

### 3. **Compare Two Stocks**
```
GET /compare?ticker1=AAPL&ticker2=MSFT
```
Side-by-side comparison with sentiment for both.

### 4. **Regenerate Insight**
```
GET /regenerate?ticker=AAPL
```
Get fresh AI perspective using alternative prompt.

### 5. **Health Check**
```
GET /health
```
Verify API and AI service status.

### 6. **List Models**
```
GET /models
```
Get available Gemini models.

### 7. **API Info**
```
GET /
```
Root API information.

## 🎁 Bonus Features Implemented

### ✅ Sentiment Classification 
- **Keyword Analysis**: Analyzes AI insight for bullish/bearish indicators
- **Keywords**:
  - Bullish: growth, strong, positive, momentum, advantage, leadership, dominance
  - Bearish: decline, negative, risk, weakness, challenge, headwind, concern
- **Sentiment Icons**: 📈 bullish / 📉 bearish / ⚖️ neutral

### ✅ Stock Comparison
- **Dual View**: Two stocks displayed side-by-side
- **Responsive**: Stacks vertically on mobile
- **VS Divider**: Clear visual separation on desktop
- **Individual Analysis**: Each stock gets own AI insight

### ✅ Regenerate Insight
- **Fresh Prompts**: Different wording for new perspectives
  - Default: "Give a one-sentence investment summary..."
  - Regenerate: "Generate a fresh, unique investment summary..."
- **Loading State**: Button shows "Regenerating..." during processing
- **One-Click Access**: Button appears in results card

### ✅ Caching Infrastructure
- **60-Second Cache**: Reduces repeated API calls
- **Backend Ready**: Uses timestamps and cache tracking
- **Smart Invalidation**: Clears on configuration change

### ✅ Complete Error Handling
- **Validation**: Input length and format checks
- **API Fallback**: Mock data when services unavailable
- **User Feedback**: Clear error messages
- **HTTP Status Codes**: Proper error responses

## 🔐 Environment Variables

Create `.env` in backend folder:

```env
# Required for AI insights
GEMINI_API_KEY=your_gemini_key

# Optional stock data source
FINNHUB_API_KEY=your_finnhub_key

# Server config
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### Getting API Keys

**Gemini API:**
1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click "Create API Key"
3. Copy and paste into .env

**Finnhub (Optional):**
1. Visit [Finnhub Dashboard](https://finnhub.io/)
2. Sign up free
3. Copy API key to .env

## 📦 Requirements.txt

```
fastapi==0.109.0
uvicorn==0.27.0
google-generativeai==0.3.1
yfinance==0.2.33
python-dotenv==1.0.0
pydantic==2.5.0
```

## 🎨 UI Features

### Modern Design
- Dark fintech theme with animated gradients
- Teal (#06d6a0) and blue (#118ab2) accent colors
- Smooth 0.3-0.5s transitions on all interactive elements
- 15-second gradient shift animation background

### Responsive Layout
- Desktop: Side-by-side compare view
- Tablet/Mobile: Stacked layout
- Touch-friendly button sizes (44px+ tap targets)
- Readable font sizes across all devices

### Animation Effects
- **Fade In/Out**: 0.5s smooth opacity transitions
- **Loading Spinner**: Continuous 1s rotation
- **Hover Effects**: Subtle scale and shadow changes
- **Tab Transitions**: Instant tab switching

### Typography
- **Headings**: Poppins 700, gradient color
- **Labels**: Poppins 600, uppercase, 0.85rem
- **Body**: Inter 400, 1rem
- **Stats**: Poppins 700, teal color, 1.5rem

## 🧪 Test Data

Available test stocks (mock data):

```
AAPL  - Apple Inc. ($228.45, +2.34%)
GOOGL - Alphabet Inc. ($154.78, -1.23%)
MSFT  - Microsoft Corporation ($391.23, +1.87%)
TSLA  - Tesla Inc. ($242.84, -3.45%)
AMZN  - Amazon.com Inc. ($178.65, +0.92%)
NVIDIA - NVIDIA Corporation ($785.93, +3.21%)
```

## 🧪 Testing

### Manual Testing Checklist

- [ ] Analyze tab: Enter "AAPL", wait 2s, view results
- [ ] Sentiment: Check icon appears (📈/📉/⚖️)
- [ ] Regenerate: Click button, get different insight
- [ ] Compare: Enter "AAPL" and "MSFT", compare
- [ ] Error: Try "INVALID", see error message
- [ ] Mobile: Resize to mobile, verify responsive
- [ ] Cache: Analyze same stock twice, second should be faster

### API Testing with cURL

```bash
curl "http://127.0.0.1:8000/analyze?ticker=AAPL"
curl "http://127.0.0.1:8000/compare?ticker1=AAPL&ticker2=MSFT"
curl "http://127.0.0.1:8000/regenerate?ticker=AAPL"
curl "http://127.0.0.1:8000/health"
```

## 📚 Code Highlights

### Sentiment Classification (ai_generator.py)
```python
def classify_sentiment(text: str) -> str:
    """Analyzes text for bullish/bearish keywords"""
    bullish_keywords = ['growth', 'strong', 'positive', ...]
    bearish_keywords = ['decline', 'negative', 'risk', ...]
    
    bullish_count = sum(1 for word in bullish_keywords if word in text.lower())
    bearish_count = sum(1 for word in bearish_keywords if word in text.lower())
    
    if bullish_count > bearish_count: return "📈 bullish"
    if bearish_count > bullish_count: return "📉 bearish"
    return "⚖️ neutral"
```

### Compare Endpoint (main.py)
```python
@app.get("/compare")
def compare_stocks(ticker1: str, ticker2: str):
    """Side-by-side stock comparison"""
    stock1 = fetch_stock_data(ticker1)
    stock2 = fetch_stock_data(ticker2)
    
    insight1 = generate_ai_insight(ticker1, stock1["price"], ...)
    insight2 = generate_ai_insight(ticker2, stock2["price"], ...)
    
    return {
        "comparison": {
            "stock1": {...},
            "stock2": {...}
        }
    }
```

### Tab Switching (index.html)
```javascript
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        switchTab(btn.dataset.tab);
    });
});

function switchTab(tabName) {
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.style.display = 'none';
    });
    document.getElementById(tabName + '-tab').style.display = 'block';
}
```

## 🚀 Deployment

### Heroku
```bash
echo "web: uvicorn main:app --host 0.0.0.0 --port \$PORT" > Procfile
heroku create app-name
git push heroku main
heroku config:set GEMINI_API_KEY=your_key
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| 401 Gemini Error | Check API key in .env, no extra spaces |
| Port 8000 in use | Use `--port 8001` flag |
| Frontend not loading | Verify backend running, check `/static` path |
| Stock data old | Restart server to clear yfinance cache |
| Compare not working | Ensure two different tickers entered |

## 💡 How GitHub Copilot Helped

GitHub Copilot accelerated development significantly:

1. **API Endpoints**: Auto-completed FastAPI structures with proper error handling (~40% code reduction)
2. **Sentiment Algorithm**: Suggested keyword lists and classification logic
3. **JavaScript Logic**: Generated tab switching, form validation, and async patterns
4. **CSS Layouts**: Responsive grid code with mobile breakpoints
5. **Error Handling**: Consistent try-catch patterns across endpoints
6. **Documentation**: FastAPI docstrings and endpoint descriptions
7. **Mock Data**: Realistic stock data for 6 companies

**Time Saved**: Estimated 30-40% reduction in development time through intelligent suggestions.

## 📊 Response Examples

### Analyze Response
```json
{
  "ticker": "AAPL",
  "price": 228.45,
  "change": "+2.34%",
  "ai_insight": "Apple continues steady growth with strong ecosystem integration.",
  "sentiment": "📈 bullish",
  "company_name": "Apple Inc.",
  "currency": "USD"
}
```

### Compare Response
```json
{
  "comparison": {
    "stock1": {
      "ticker": "AAPL",
      "price": 228.45,
      "sentiment": "📈 bullish",
      ...
    },
    "stock2": {
      "ticker": "MSFT",
      "price": 391.23,
      "sentiment": "📈 bullish",
      ...
    }
  }
}
```

## 📄 License

MIT License - Feel free to use this project

## 🙏 Acknowledgments

- Google Gemini API for AI insights
- Yahoo Finance for stock data
- FastAPI framework
- GitHub Copilot for development assistance

---

## Ready to Run?

```bash
# Terminal 1: Start backend
cd backend
uvicorn main:app --reload

# Terminal 2: Open frontend
# Navigate to: http://127.0.0.1:8000/static/index.html
```

**Enjoy analyzing stocks! 📈**
