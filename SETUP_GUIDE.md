# Complete Setup Guide - Physical AI RAG Chatbot

## Step-by-Step Instructions

### STEP 1: Get Free API Keys

#### A. Google Gemini (Free - No Credit Card)
1. Visit https://ai.google.dev
2. Click "Get API Key in Google AI Studio"
3. Sign in with Google account
4. Click "Create API Key"
5. Copy the key

#### B. Qdrant Cloud (Free Tier)
1. Visit https://cloud.qdrant.io
2. Sign up (GitHub/Google)
3. Create new cluster (Free 1GB)
4. Go to "Data Access Control"
5. Copy Cluster URL and API Key

#### C. Neon Postgres (Free Tier)
1. Visit https://neon.tech
2. Sign up
3. Create new project
4. Copy connection string from dashboard

---

### STEP 2: Setup Backend

```bash
# Navigate to backend folder
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env
```

Edit `.env` with your keys:
```
GEMINI_API_KEY=AIzaSy...
QDRANT_URL=https://xyz.qdrant.io
QDRANT_API_KEY=your_key
NEON_DATABASE_URL=postgresql://user:pass@host/db
```

---

### STEP 3: Run Backend Locally

```bash
# Start the server
python main.py
```

Backend runs at: http://localhost:8000

Test it: Open http://localhost:8000 in browser

---

### STEP 4: Ingest Course Documents

```bash
# Go back to project root
cd ..

# Run ingestion script
python scripts/smart_ingest.py
```

This loads all course content into Qdrant vector database.

---

### STEP 5: Update Frontend Configuration

Edit `src/config.ts`:

```typescript
// Change this line:
let internalApiUrl = 'http://localhost:8000';
```

---

### STEP 6: Run Frontend

```bash
# Install dependencies (if not done)
npm install

# Start development server
npm start
```

Frontend runs at: http://localhost:3000

---

### STEP 7: Test the Chatbot

1. Open http://localhost:3000
2. Click chat icon
3. Ask: "What is Physical AI?"
4. Select text and ask questions about it

---

## Deploy to Production

### Deploy Backend (Render - Free)

1. Push code to GitHub
2. Go to https://render.com
3. New → Web Service
4. Connect your repo
5. Settings:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
6. Add environment variables
7. Deploy

Copy your backend URL (e.g., `https://your-app.onrender.com`)

### Deploy Frontend (GitHub Pages)

1. Update `docusaurus.config.ts`:
   ```typescript
   url: 'https://YOUR_USERNAME.github.io',
   organizationName: 'YOUR_USERNAME',
   projectName: 'YOUR_REPO_NAME',
   ```

2. Update `src/config.ts`:
   ```typescript
   let internalApiUrl = 'https://your-backend.onrender.com';
   ```

3. Deploy:
   ```bash
   npm run deploy
   ```

4. Enable GitHub Pages in repo settings

---

## Troubleshooting

**Backend won't start:**
- Check all API keys in `.env`
- Verify Python 3.8+ installed

**Ingestion fails:**
- Ensure backend is running
- Check `API_URL` in `smart_ingest.py`

**Chat not working:**
- Verify backend URL in `src/config.ts`
- Check browser console for errors
- Ensure documents are ingested

**CORS errors:**
- Backend already has CORS enabled
- Check frontend is using correct URL

---

## Cost Breakdown (All Free Tiers)

- Google Gemini: 15 requests/min (Free)
- Qdrant Cloud: 1GB storage (Free)
- Neon Postgres: 0.5GB storage (Free)
- Render: 750 hours/month (Free)
- GitHub Pages: Unlimited (Free)

**Total Cost: $0/month**
