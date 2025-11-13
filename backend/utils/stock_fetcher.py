"""Stock data fetcher module using yfinance"""
import yfinance as yf
from typing import Dict

MOCK_STOCKS = {
    "AAPL": {"price": 187.50, "change": 1.2, "currency": "USD", "name": "Apple Inc."},
    "GOOGL": {"price": 156.23, "change": 2.1, "currency": "USD", "name": "Alphabet Inc."},
    "MSFT": {"price": 373.49, "change": 1.8, "currency": "USD", "name": "Microsoft Corporation"},
    "TSLA": {"price": 278.95, "change": -0.5, "currency": "USD", "name": "Tesla Inc."},
    "AMZN": {"price": 194.85, "change": 0.9, "currency": "USD", "name": "Amazon.com Inc."}
}


def fetch_stock_data(ticker: str) -> Dict:
    """Fetch stock data using yfinance with fallback to mock data."""
    if not ticker or not isinstance(ticker, str):
        raise ValueError("Ticker must be a non-empty string")
    
    ticker = ticker.upper().strip()
    
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        if not info or "regularMarketPrice" not in info:
            raise ValueError(f"No data found for ticker: {ticker}")
        
        return {
            "price": info.get("regularMarketPrice"),
            "change": round(info.get("regularMarketChangePercent", 0), 2),
            "currency": info.get("currency", "USD"),
            "name": info.get("longName", ticker),
            "source": "Yahoo Finance"
        }
    except Exception as e:
        print(f"Error fetching real data for {ticker}: {str(e)}")
        if ticker in MOCK_STOCKS:
            return {**MOCK_STOCKS[ticker], "source": "Mock Data (API Unavailable)"}
        raise ValueError(f"Stock ticker '{ticker}' not found and no mock data available")


def format_change(change: float) -> str:
    """Format change percentage with sign."""
    sign = "+" if change >= 0 else ""
    return f"{sign}{change:.2f}%"
