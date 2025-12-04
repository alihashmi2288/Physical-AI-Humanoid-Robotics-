from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import *
from rag import ingest_document, search_documents, generate_response
from database import init_qdrant, init_neon
from auth import init_auth_tables, signup_user, login_user
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Physical AI RAG Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize on module load for Vercel
try:
    init_qdrant()
    init_neon()
    init_auth_tables()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except Exception as e:
    print(f"Initialization warning: {e}")

@app.get("/")
async def root():
    return {"status": "Physical AI RAG Backend Running", "model": "Gemini 2.5 Flash"}

@app.post("/api/auth/sign-up/email")
async def signup(request: SignupRequest):
    """User signup"""
    return signup_user(request.email, request.password, request.name)

@app.post("/api/auth/sign-in/email")
async def login(request: LoginRequest):
    """User login"""
    return login_user(request.email, request.password)

@app.post("/api/ingest")
async def ingest(request: IngestRequest):
    """Ingest document for RAG"""
    try:
        point_id = ingest_document(request.text, request.metadata)
        return {"status": "success", "id": point_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint with RAG"""
    try:
        user_message = request.history[-1].content
        
        # Search relevant documents
        docs = search_documents(user_message, limit=3)
        context = "\n\n".join([doc["text"][:500] for doc in docs])
        
        # Generate response
        history = [{"role": msg.role, "content": msg.content} for msg in request.history]
        response = generate_response(user_message, context, history)
        
        sources = [{"title": doc["source"], "url": ""} for doc in docs]
        
        return ChatResponse(response=response, sources=sources)
    except Exception as e:
        import traceback
        print(f"ERROR in chat endpoint: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat/selected")
async def selected_chat(request: SelectedChatRequest):
    """Chat about selected text"""
    try:
        prompt = f"""The user selected this text from the course:

"{request.selected_text}"

User question: {request.user_query}

Explain this clearly based on the selected text."""
        
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/latest-developments", response_model=LatestResponse)
async def latest_developments(request: LatestRequest):
    """Get latest research developments"""
    try:
        prompt = f"""Provide the latest research developments and breakthroughs in {request.book_section} 
for Physical AI and Robotics. Focus on papers from 2024-2025. Format as markdown with bullet points."""
        
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        
        return LatestResponse(
            response=response.text,
            reasoning=f"Searched for latest research in {request.book_section}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# For Vercel serverless - export the app directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
