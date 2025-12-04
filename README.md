# Physical AI Learning Platform

An intelligent, adaptive educational platform for Physical AI and Humanoid Robotics featuring AI-powered assistance, multilingual support, and personalized learning experiences.

## 🌟 Features

- **AI-Powered Chatbot**: RAG-based assistant trained on course content using Google Gemini 2.5 Flash
- **Adaptive Learning**: Content automatically adjusts between Beginner and Advanced levels
- **Multilingual Support**: Seamless switching between English and Urdu with RTL support
- **Interactive Components**: React-based simulations, code blocks, and visualizations
- **User Authentication**: Secure signup/login with session management
- **Text Selection Chat**: Ask questions about any selected text on the page
- **Latest Research**: Real-time updates on Physical AI developments

## 🛠️ Tech Stack

### Frontend
- **Framework**: Docusaurus 3.9.2 with React 19
- **Language**: TypeScript 5.6.2
- **Styling**: TailwindCSS 3.4.1
- **Content**: MDX with Mermaid diagrams
- **Math**: KaTeX for mathematical notation

### Backend
- **API**: FastAPI (Python)
- **AI Model**: Google Gemini 2.5 Flash
- **Vector DB**: Qdrant Cloud (embeddings & semantic search)
- **Database**: Neon Serverless Postgres (user data & metadata)
- **Authentication**: JWT-based auth

## 📋 Prerequisites

- **Node.js**: >= 20.0
- **Python**: >= 3.8
- **Git**: For version control

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Setup Backend

#### Get API Keys (All Free)

**Google Gemini:**
1. Visit https://ai.google.dev
2. Click "Get API Key"
3. Copy your API key

**Qdrant Cloud:**
1. Visit https://cloud.qdrant.io
2. Create free cluster (1GB)
3. Copy Cluster URL and API Key

**Neon Postgres:**
1. Visit https://neon.tech
2. Create project
3. Copy connection string

#### Configure Backend

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env
```

Edit `.env` with your keys:
```env
GEMINI_API_KEY=your_gemini_api_key
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=postgresql://user:pass@host/db
JWT_SECRET=your-random-secret-key
```

#### Start Backend

```bash
python main.py
```

Backend runs at: http://localhost:8000

### 3. Ingest Course Content

```bash
# From project root
python scripts/smart_ingest.py
```

This loads all course materials into Qdrant vector database.

### 4. Setup Frontend

```bash
# From project root
npm install
```

Update `src/config.ts`:
```typescript
let internalApiUrl = 'http://localhost:8000'; // For local development
```

Update `docusaurus.config.ts`:
```typescript
url: 'https://YOUR_USERNAME.github.io',
organizationName: 'YOUR_USERNAME',
projectName: 'YOUR_REPO_NAME',
baseUrl: '/', // For local dev, use '/YOUR_REPO_NAME/' for GitHub Pages
```

### 5. Run Frontend

```bash
npm start
```

Frontend runs at: http://localhost:3000

## 📚 Course Structure

```
docs/
├── module-1/          # ROS 2 Fundamentals
├── module-2/          # Simulation (Gazebo & Unity)
├── module-3/          # NVIDIA Isaac Platform
├── module-4/          # Vision-Language-Action
└── capstone/          # Final Project
```

## 🌐 Deployment

### Deploy Backend (Vercel)

```bash
cd backend
npm install -g vercel
vercel login
vercel
```

Add environment variables in Vercel dashboard, then:
```bash
vercel --prod
```

### Deploy Frontend (GitHub Pages)

Update `docusaurus.config.ts`:
```typescript
baseUrl: '/YOUR_REPO_NAME/',
```

Update `src/config.ts`:
```typescript
let internalApiUrl = 'https://your-backend.vercel.app';
```

Deploy:
```bash
npm run deploy
```

Site will be live at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

## 🔧 Development

### Project Structure

```
├── backend/              # FastAPI backend
│   ├── main.py          # API endpoints
│   ├── rag.py           # RAG implementation
│   ├── auth.py          # Authentication
│   └── database.py      # DB connections
├── docs/                # Course content (MDX)
├── src/
│   ├── components/      # React components
│   ├── pages/          # Static pages
│   ├── services/       # API services
│   └── contexts/       # React contexts
├── scripts/            # Utility scripts
└── static/             # Static assets
```

### Key Commands

```bash
# Frontend
npm start              # Development server
npm run build         # Production build
npm run deploy        # Deploy to GitHub Pages

# Backend
python main.py        # Start server
python scripts/smart_ingest.py  # Ingest content
```

## 🎯 Features Guide

### Using the Chatbot
1. Click chat icon (bottom right)
2. Login/Signup if not authenticated
3. Ask questions about course content
4. Chatbot uses RAG to provide accurate answers

### Text Selection Chat
1. Select any text on a page
2. Click the chat icon that appears
3. Ask questions about the selected content

### Personalization
1. Complete the quiz after signup
2. Choose Beginner or Advanced level
3. Select preferred language (English/Urdu)
4. Content adapts automatically

### Latest Research
1. Click "Latest Research" button on any page
2. View recent developments in that topic
3. AI fetches and summarizes latest papers

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

**Backend won't start:**
- Verify all API keys in `.env`
- Check Python version (>= 3.8)

**Chatbot not working:**
- Ensure backend is running
- Check `src/config.ts` has correct backend URL
- Verify documents are ingested

**Build errors:**
- Run `npm install` again
- Clear cache: `npm run clear`
- Check Node version (>= 20.0)

## 📧 Support

For issues and questions, please open an issue on GitHub.

---

Built with ❤️ for Physical AI Education
