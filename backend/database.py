import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Qdrant setup
_qdrant_client = None

COLLECTION_NAME = "physical_ai_docs"

def get_qdrant_client():
    global _qdrant_client
    if _qdrant_client is None:
        _qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY")
        )
    return _qdrant_client

def init_qdrant():
    """Initialize Qdrant collection if not exists"""
    client = get_qdrant_client()
    try:
        client.get_collection(COLLECTION_NAME)
    except:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE)
        )

def get_neon_connection():
    """Get Neon Postgres connection"""
    return psycopg2.connect(os.getenv("NEON_DATABASE_URL"))

def init_neon():
    """Initialize Neon database tables"""
    conn = get_neon_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id SERIAL PRIMARY KEY,
            source TEXT,
            path TEXT,
            ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
