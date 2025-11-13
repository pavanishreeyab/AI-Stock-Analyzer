"""AI insight generator using Google Gemini API"""
import google.generativeai as genai

MOCK_INSIGHTS = {
    "AAPL": "Apple continues steady growth with strong ecosystem integration and services momentum.",
    "GOOGL": "Alphabet demonstrates robust AI leadership and cloud growth potential.",
    "MSFT": "Microsoft leverages dominant cloud position with expanding AI capabilities.",
    "TSLA": "Tesla navigates competitive EV landscape with innovation focus.",
    "AMZN": "Amazon maintains market leadership with AWS dominance and advertising growth."
}


def generate_ai_insight(ticker: str, price: float, change: float) -> str:
    """Generate AI insight using Gemini API with mock fallback."""
    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        prompt = f"""Give a one-sentence investment summary for {ticker} stock 
        (current price: ${price:.2f}, change: {change:+.2f}%), 
        focusing on current market trends. Keep it concise."""
        
        response = model.generate_content(prompt)
        return response.text.strip() if response and response.text else get_mock_insight(ticker)
    except:
        return get_mock_insight(ticker)


def get_mock_insight(ticker: str) -> str:
    """Get mock insight for ticker."""
    return MOCK_INSIGHTS.get(ticker.upper(), 
                           f"{ticker} shows market movement with investor interest in current trends.")


def validate_api_key() -> bool:
    """Check if Gemini API key is configured."""
    try:
        genai.get_model("models/gemini-2.5-flash")
        return True
    except:
        return False
