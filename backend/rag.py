import os
import google.generativeai as genai
from qdrant_client.models import PointStruct
from database import qdrant_client, COLLECTION_NAME, get_neon_connection
from dotenv import load_dotenv
import uuid

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding(text: str):
    """Generate embeddings using Gemini"""
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=text,
        task_type="retrieval_document"
    )
    return result['embedding']

def ingest_document(text: str, metadata: dict):
    """Ingest document into Qdrant and Neon"""
    # Generate embedding
    embedding = get_embedding(text)
    
    # Store in Qdrant
    point_id = str(uuid.uuid4())
    qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=point_id,
                vector=embedding,
                payload={"text": text, **metadata}
            )
        ]
    )
    
    # Store metadata in Neon
    conn = get_neon_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO documents (source, path) VALUES (%s, %s)",
        (metadata.get("source"), metadata.get("path"))
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return point_id

def search_documents(query: str, limit: int = 3):
    """Search similar documents using RAG"""
    query_embedding = get_embedding(query)
    
    results = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=limit
    )
    
    return [
        {
            "text": hit.payload["text"],
            "source": hit.payload.get("source", "Unknown"),
            "score": hit.score
        }
        for hit in results
    ]

def generate_response(query: str, context: str, history: list = None):
    """Generate response using Gemini with RAG context"""
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""You are an expert AI assistant for a Physical AI and Robotics course.
Use the following context from the course materials to answer the question.

Context:
{context}

Question: {query}

Provide a clear, accurate answer based on the context. If the context doesn't contain enough information, say so."""
    
    if history:
        # Map assistant role to model for Gemini
        gemini_history = []
        for msg in history[:-1]:
            role = "model" if msg["role"] == "assistant" else "user"
            gemini_history.append({"role": role, "parts": [msg["content"]]})
        
        chat = model.start_chat(history=gemini_history)
        response = chat.send_message(prompt)
    else:
        response = model.generate_content(prompt)
    
    return response.text
