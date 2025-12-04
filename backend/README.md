# Physical AI RAG Backend

RAG chatbot backend using Google Gemini, Qdrant, and Neon Postgres.

## Setup

### 1. Get API Keys

**Google Gemini (Free):**
- Go to https://ai.google.dev
- Click "Get API Key"
- Create new project and get key

**Qdrant Cloud (Free):**
- Go to https://cloud.qdrant.io
- Sign up and create free cluster
- Get URL and API key

**Neon Postgres (Free):**
- Go to https://neon.tech
- Create account and database
- Copy connection string

### 2. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Configure Environment

Create `.env` file:
```
GEMINI_API_KEY=your_gemini_key
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your_qdrant_key
NEON_DATABASE_URL=postgresql://user:pass@host/db
```

### 4. Run Backend

```bash
python main.py
```

Backend runs on http://localhost:8000

### 5. Ingest Documents

```bash
cd ..
python scripts/smart_ingest.py
```

Update `API_URL` in `smart_ingest.py` to `http://localhost:8000/api/ingest`

### 6. Update Frontend

In `src/config.ts`:
```typescript
let internalApiUrl = 'http://localhost:8000';
```

## Deploy

**Vercel (Recommended):**
- Install Vercel CLI: `npm i -g vercel`
- Run: `vercel`
- Add environment variables in Vercel dashboard

**Render:**
- Connect GitHub repo
- Select `backend` folder
- Add environment variables

**Railway:**
- Connect repo
- Deploy from `backend` folder
- Add environment variables
