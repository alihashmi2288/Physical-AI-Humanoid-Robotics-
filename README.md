# Physical AI Learning Platform

An intelligent, adaptive educational platform for Physical AI and Humanoid Robotics featuring AI-powered assistance, multilingual support, and personalized learning experiences.

## 🌟 Features

- **AI-Powered Chatbot**: RAG-based assistant trained on course content using Google Gemini 2.5 Flash.
- **Adaptive Learning**: Content automatically adjusts between **Novice** and **Professional** levels based on user preference.
- **Multilingual Support**: Seamless switching between **English** and **Urdu** with full RTL layout support.
- **Personalization Quiz**: Onboarding quiz to tailor the learning experience to the user's background.
- **Interactive Components**: React-based simulations, code blocks, and visualizations.
- **User Authentication**: Secure signup/login with JWT-based session management and profile customization.
- **Text Selection Chat**: Contextual AI assistance by selecting any text on the page.
- **Latest Research**: Real-time updates on Physical AI developments fetched via AI.

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

## 🧠 Spec-Driven Development

This project utilizes **SpecKit Plus** for a structured, AI-assisted development workflow known as **Spec-Driven Development (SDD)**.

### Core Philosophy
- **Specs First**: All features start with a clear specification in `specs/`.
- **Planning**: Architectural decisions are documented in `implementation_plan.md` before code is written.
- **History**: Every interaction and decision is recorded in `history/prompts/` and `history/adr/`.

### Directory Structure
- `specs/`: Feature specifications, plans, and task lists.
- `history/prompts/`: Verbatim records of every user prompt and AI response (PHR).
- `history/adr/`: Architectural Decision Records (ADR) for significant technical choices.
- `.specify/`: Configuration and templates for the AI agent.

### Workflow
1.  **Spec**: Define requirements in `specs/<feature>/spec.md`.
2.  **Plan**: Create a technical plan in `specs/<feature>/plan.md`.
3.  **Task**: Break down work into testable tasks in `specs/<feature>/tasks.md`.
4.  **Execute**: Implement changes while maintaining the `task.md` checklist.

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/alihashmi2288/Physical-AI-Humanoid-Robotics-.git
cd Physical-AI-Humanoid-Robotics-
```

### 2. Get Free API Keys

You will need API keys for the backend services. All offer generous free tiers.

#### A. Google Gemini
1. Visit [Google AI Studio](https://ai.google.dev).
2. Click "Get API Key".
3. Copy your API key.

#### B. Qdrant Cloud
1. Visit [Qdrant Cloud](https://cloud.qdrant.io).
2. Create a free cluster (1GB).
3. Copy the **Cluster URL** and **API Key**.

#### C. Neon Postgres
1. Visit [Neon](https://neon.tech).
2. Create a project.
3. Copy the **Connection String**.

### 3. Setup Backend

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

### 4. Run Backend & Ingest Content

Start the backend server:
```bash
python main.py
```
*Backend runs at: http://localhost:8000*

Open a new terminal to ingest course content into the vector database:
```bash
# From project root
python scripts/smart_ingest.py
```

### 5. Setup & Run Frontend

```bash
# From project root
npm install
```

Update `src/config.ts` for local development:
```typescript
export const USE_MOCK_API = false;
let internalApiUrl = 'http://localhost:8000';
```

Start the frontend:
```bash
npm start
```
*Frontend runs at: http://localhost:3000*

## � Project Structure

```
├── backend/                # FastAPI Backend
│   ├── main.py            # API Entry point & Endpoints
│   ├── auth.py            # Authentication logic (JWT, Login, Signup)
│   ├── rag.py             # RAG (Retrieval Augmented Generation) logic
│   ├── database.py        # Database connection & models
│   └── requirements.txt   # Python dependencies
├── docs/                  # Course Content (MDX files)
│   ├── module-1/          # Module 1 content
│   └── ...
├── src/                   # Frontend Source
│   ├── components/        # React Components
│   │   ├── AuthNavbarItem/      # Login/Profile dropdown in navbar
│   │   ├── ChatWidget/          # AI Chatbot widget
│   │   ├── PersonalizationQuiz/ # Onboarding quiz
│   │   └── ...
│   ├── contexts/          # React Contexts
│   │   ├── AuthContext.tsx      # User authentication state
│   │   └── PersonalizationProvider.tsx # User preferences state
│   ├── pages/             # Static Pages (Home, Login, Profile)
│   └── theme/             # Docusaurus Theme Customizations
├── specs/                 # Spec-Driven Development
│   ├── 001-platform-setup/ # Initial setup specs
│   └── 002-Physical-AI-Book/ # Feature specs
├── history/               # Project History
│   ├── prompts/           # Prompt History Records (PHR)
│   └── adr/               # Architectural Decision Records (ADR)
├── scripts/               # Utility Scripts
│   └── smart_ingest.py    # Script to ingest docs into Qdrant
├── docusaurus.config.ts   # Docusaurus Configuration
└── tailwind.config.js     # Tailwind CSS Configuration
```

## 📚 Course Structure

```
docs/
├── module-1/          # ROS 2 Fundamentals
├── module-2/          # Simulation (Gazebo & Unity)
├── module-3/          # NVIDIA Isaac Platform
├── module-4/          # Vision-Language-Action
└── capstone/          # Final Project
```

## � Deployment

### Deploy Backend (Vercel)
1. Push code to GitHub.
2. Import your repository on [Vercel](https://vercel.com).
3. Set Root Directory to `backend`.
4. Vercel will automatically detect Python.
5. Add environment variables from your `.env`.
6. Deploy.

### Deploy Frontend (GitHub Pages)
1. Update `docusaurus.config.ts`:
   ```typescript
   url: 'https://alihashmi2288.github.io',
   baseUrl: '/Physical-AI-Humanoid-Robotics-/',
   projectName: 'Physical-AI-Humanoid-Robotics-',
   ```
2. Update `src/config.ts` with your production backend URL (e.g., `https://your-project.vercel.app`).
3. Deploy:
   ```bash
   npm run deploy
   ```

## 💰 Cost Breakdown (Free Tier)

This project is designed to run entirely on free tiers of modern cloud services:

| Service | Usage | Free Tier Limit |
|---------|-------|-----------------|
| **Google Gemini** | AI Model | 15 requests/min |
| **Qdrant Cloud** | Vector DB | 1GB Storage |
| **Neon Postgres** | Database | 0.5GB Storage |
| **Vercel** | Backend Hosting | 100 GB-hours/month |
| **GitHub Pages** | Frontend Hosting | Unlimited |

**Total Cost: $0/month**

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
- Verify all API keys in `.env` are correct.
- Ensure you are using Python 3.8 or higher.

**Chatbot not working:**
- Ensure backend is running and accessible.
- Check `src/config.ts` has the correct `internalApiUrl`.
- Verify documents have been ingested using `smart_ingest.py`.

**Session/Login Issues:**
- If reloading the page causes errors, ensure you are on the latest version (fixed in recent updates).
- Clear browser cookies/local storage if stuck in an invalid state.

## 📧 Support

For issues and questions, please open an issue on GitHub.

---

Built by Syed Ali Hashmi
