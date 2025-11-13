// Mock Stock Database
const stockDatabase = {
    'AAPL': {
        name: 'Apple Inc.',
        price: 195.42,
        change: 2.34,
        volume: 52380000
    },
    'GOOGL': {
        name: 'Alphabet Inc.',
        price: 140.28,
        change: -1.23,
        volume: 21430000
    },
    'MSFT': {
        name: 'Microsoft Corp.',
        price: 378.91,
        change: 1.87,
        volume: 18920000
    },
    'TSLA': {
        name: 'Tesla Inc.',
        price: 242.84,
        change: -3.45,
        volume: 92450000
    },
    'AMZN': {
        name: 'Amazon Inc.',
        price: 178.65,
        change: 0.92,
        volume: 42180000
    }
};

// Mock AI Insights Database
const insightsDatabase = {
    'AAPL': 'Apple continues to dominate the premium smartphone market with strong services revenue. Consider buying on dips as the ecosystem loyalty remains strong. Technical support levels at $185 and resistance at $200.',
    'GOOGL': 'Alphabet faces regulatory scrutiny but advertising fundamentals remain solid. Watch for AI integration announcements. Recent sell-off presents buying opportunity for long-term investors.',
    'MSFT': 'Microsoft\'s cloud business (Azure) shows exceptional growth. AI initiatives with OpenAI partnership are game-changing. Strong dividend yield makes this attractive for value investors.',
    'TSLA': 'Tesla stock shows volatility due to macro factors and competition. However, EV adoption accelerates. Earnings potential remains strong. Monitor semi-annual guidance closely.',
    'AMZN': 'Amazon\'s cloud division (AWS) is profit powerhouse. E-commerce growth stabilizes. Good entry point for patient long-term investors. Support at $170.'
};

// DOM Elements
const tickerInput = document.getElementById('ticker-input');
const analyzeBtn = document.getElementById('analyze-btn');
const loadingContainer = document.getElementById('loading-container');
const outputCard = document.getElementById('output-card');

// Event Listeners
analyzeBtn.addEventListener('click', handleAnalyze);
tickerInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleAnalyze();
});

// Main Analysis Function
async function handleAnalyze() {
    const ticker = tickerInput.value.trim().toUpperCase();
    
    if (!ticker) {
        alert('Please enter a stock ticker');
        return;
    }
    
    analyzeBtn.disabled = true;
    loadingContainer.classList.remove('hidden');
    outputCard.classList.add('hidden');
    
    try {
        // Try to fetch from backend API
        const response = await fetch(`http://127.0.0.1:8000/analyze?ticker=${ticker}`);
        
        if (response.ok) {
            const data = await response.json();
            displayResults(data);
        } else {
            // Fallback to mock data
            displayMockResults(ticker);
        }
    } catch (error) {
        // Fallback to mock data if backend is down
        displayMockResults(ticker);
    } finally {
        analyzeBtn.disabled = false;
        loadingContainer.classList.add('hidden');
        outputCard.classList.remove('hidden');
    }
}

// Display Results from Backend API
function displayResults(data) {
    const stock = data.stock_data;
    const insight = data.ai_insight;
    
    document.getElementById('stock-name').textContent = stock.name;
    document.getElementById('stock-ticker').textContent = stock.ticker;
    document.getElementById('stock-price').textContent = `$${stock.price.toFixed(2)}`;
    
    const changeElement = document.getElementById('stock-change');
    const changePercentage = ((stock.change / stock.price) * 100).toFixed(2);
    const changeText = stock.change >= 0 
        ? `+${stock.change.toFixed(2)} (+${changePercentage}%)`
        : `${stock.change.toFixed(2)} (${changePercentage}%)`;
    
    changeElement.textContent = changeText;
    changeElement.className = `change ${stock.change >= 0 ? 'positive' : 'negative'}`;
    
    document.getElementById('ai-summary').textContent = insight || 'Market analysis in progress...';
    document.getElementById('market-cap').textContent = `$${(stock.price * stock.volume / 1e9).toFixed(2)}B`;
    document.getElementById('volume').textContent = `${(stock.volume / 1e6).toFixed(2)}M`;
    document.getElementById('pe-ratio').textContent = '24.5';
    document.getElementById('dividend').textContent = '0.92%';
}

// Display Mock Results (Fallback)
function displayMockResults(ticker) {
    const stock = stockDatabase[ticker];
    const insight = insightsDatabase[ticker];
    
    if (!stock) {
        alert(`Sorry, "${ticker}" data not available. Try: AAPL, GOOGL, MSFT, TSLA, AMZN`);
        loadingContainer.classList.add('hidden');
        outputCard.classList.add('hidden');
        return;
    }
    
    document.getElementById('stock-name').textContent = stock.name;
    document.getElementById('stock-ticker').textContent = ticker;
    document.getElementById('stock-price').textContent = `$${stock.price.toFixed(2)}`;
    
    const changeElement = document.getElementById('stock-change');
    const changePercentage = ((stock.change / stock.price) * 100).toFixed(2);
    const changeText = stock.change >= 0 
        ? `+${stock.change.toFixed(2)} (+${changePercentage}%)`
        : `${stock.change.toFixed(2)} (${changePercentage}%)`;
    
    changeElement.textContent = changeText;
    changeElement.className = `change ${stock.change >= 0 ? 'positive' : 'negative'}`;
    
    document.getElementById('ai-summary').textContent = insight;
    document.getElementById('market-cap').textContent = `$${(stock.price * stock.volume / 1e9).toFixed(2)}B`;
    document.getElementById('volume').textContent = `${(stock.volume / 1e6).toFixed(2)}M`;
    document.getElementById('pe-ratio').textContent = Math.random() < 0.5 ? '18.5' : '22.3';
    document.getElementById('dividend').textContent = (Math.random() * 3 + 0.5).toFixed(2) + '%';
}

// Set initial focus
tickerInput.focus();
