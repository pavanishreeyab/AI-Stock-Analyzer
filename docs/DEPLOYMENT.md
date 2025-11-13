````markdown
# DEPLOYMENT GUIDE - Stock Analyzer Backend

## Production Deployment Options

### Option 1: Local Production (Recommended for Learning)

```bash
# Install production server
pip install gunicorn

# Run with Gunicorn (4 workers)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --host 0.0.0.0 --port 8000
```

### Option 2: Docker Deployment

**Create `Dockerfile`:**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Build and run:**
```bash
docker build -t stock-analyzer .
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key stock-analyzer
```

### Option 3: Cloud Deployment

#### **Heroku**
```bash
# Create Procfile
echo "web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app" > Procfile

# Deploy
heroku login
heroku create stock-analyzer-app
heroku config:set GEMINI_API_KEY=your_key
git push heroku main
```

#### **AWS EC2**
```bash
# SSH into instance
ssh -i key.pem ec2-user@your-instance-ip

# Clone repo
git clone your-repo
cd backend

# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run with nohup (background)
nohup gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000 > app.log 2>&1 &
```

#### **Google Cloud Run**
```bash
# Create cloudbuild.yaml
gcloud run deploy stock-analyzer \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars GEMINI_API_KEY=your_key
```

#### **Railway.app** (Easiest)
1. Push repo to GitHub
2. Go to https://railway.app
3. Connect GitHub repo
4. Add environment variables
5. Deploy

#### **Render**
1. Connect GitHub
2. Create Web Service
3. Set environment variables
4. Deploy

### Option 4: Using PM2 (Node Process Manager - for Linux/Mac)

```bash
# Install PM2
npm install -g pm2

# Create PM2 config (ecosystem.config.js)
module.exports = {
  apps: [{
    name: 'stock-analyzer',
    script: 'python',
    args: '-m uvicorn main:app --host 0.0.0.0 --port 8000',
    env: {
      GEMINI_API_KEY: 'your_key_here'
    }
  }]
};

# Start with PM2
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

## Environment Variables

### Required
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Optional
```env
PORT=8000
HOST=0.0.0.0
LOG_LEVEL=info
```

### Setting Environment Variables

**Linux/Mac (shell):**
```bash
export GEMINI_API_KEY=your_key
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your_key"
```

**Docker:**
```bash
docker run -e GEMINI_API_KEY=your_key -p 8000:8000 stock-analyzer
```

**Heroku:**
```bash
heroku config:set GEMINI_API_KEY=your_key
```

**Railway/Render/Cloud Run:**
Use their dashboard to add environment variables

## Monitoring & Logging

### Using Gunicorn with Logging

```bash
gunicorn -w 4 \
  -k uvicorn.workers.UvicornWorker \
  --access-logfile - \
  --error-logfile - \
  --log-level debug \
  main:app
```

### Using Nginx as Reverse Proxy

**`/etc/nginx/sites-available/default`:**
```nginx
upstream stock_analyzer {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://stock_analyzer;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### SSL/HTTPS with Let's Encrypt

```bash
# Install certbot
sudo apt-get install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d your-domain.com

# Auto-renew
sudo certbot renew --dry-run
```

## Performance Optimization

### 1. Enable Caching

Add to `main.py`:
```python
from fastapi.responses import JSONResponse

@app.get("/analyze")
def analyze_stock(ticker: str):
    # ... existing code ...
    
    # Cache response for 5 minutes
    response = JSONResponse(content=result)
    response.headers["Cache-Control"] = "public, max-age=300"
    return response
```

### 2. Add Rate Limiting

```bash
pip install slowapi
```

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/analyze")
@limiter.limit("30/minute")
def analyze_stock(ticker: str):
    # ...
```

### 3. Database Caching

```python
# Add Redis caching
pip install redis

from redis import Redis
redis_client = Redis(host='localhost', port=6379, db=0)

@app.get("/analyze")
def analyze_stock(ticker: str):
    cache_key = f"stock:{ticker}"
    cached = redis_client.get(cache_key)
    
    if cached:
        return json.loads(cached)
    
    # ... fetch and cache ...
    redis_client.setex(cache_key, 300, json.dumps(result))
    return result
```

## Monitoring Health

### Health Check Endpoint

Your API already has: `GET /health`

```bash
curl http://your-api.com/health
```

Monitor with:
- Healthchecks.io
- UptimeRobot
- Pingdom
- CloudFlare

### Logging to External Service

```python
import logging
from pythonjsonlogger import jsonlogger

# Setup JSON logging for ELK/CloudWatch
handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(handler)
```

## Security Checklist

- [ ] Never commit `.env` file
- [ ] Use strong API keys
- [ ] Enable HTTPS/SSL
- [ ] Set rate limiting
- [ ] Validate all inputs (already done)
- [ ] Use environment variables for secrets
- [ ] Enable CORS only for trusted domains
- [ ] Add authentication if needed
- [ ] Keep dependencies updated
- [ ] Use secret management (HashiCorp Vault, AWS Secrets)

## Update Security Headers

```python
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["yourdomain.com", "www.yourdomain.com"]
)
```

## Scaling Strategy

### Horizontal Scaling (Multiple Instances)

1. **Load Balancer** (Nginx/HAProxy) → Multiple API instances
2. **Redis Cache** → Shared across instances
3. **Database** → Centralized PostgreSQL/MongoDB
4. **Celery** → Background jobs for AI analysis

### Vertical Scaling (Single Powerful Instance)

1. Increase workers: `-w 16` (4 × CPU cores)
2. Increase memory allocation
3. Optimize database queries
4. Enable caching

## Deployment Checklist

- [ ] Update dependencies: `pip install --upgrade -r requirements.txt`
- [ ] Test locally: `python examples.py`
- [ ] Set environment variables
- [ ] Enable HTTPS
- [ ] Configure logging
- [ ] Setup monitoring
- [ ] Test all endpoints
- [ ] Setup auto-backups
- [ ] Document deployment steps
- [ ] Setup CI/CD pipeline

## Rollback Plan

```bash
# Keep previous version
git tag v1.0.0
git push origin v1.0.0

# Rollback if needed
git checkout v1.0.0
```

## Support Resources

- FastAPI Deployment: https://fastapi.tiangolo.com/deployment/
- Gunicorn Docs: https://docs.gunicorn.org/
- Railway.app: https://railway.app/docs
- Render: https://render.com/docs

---

**Ready to deploy?** Pick your preferred option above and follow the steps!

````
