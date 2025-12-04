import os
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Header
from database import get_neon_connection
import hashlib

SECRET_KEY = os.getenv("JWT_SECRET", "your-secret-key-change-in-production")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_token(user_id: str, email: str) -> str:
    payload = {
        "user_id": user_id,
        "email": email,
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

def init_auth_tables():
    conn = get_neon_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def signup_user(email: str, password: str, name: str):
    conn = get_neon_connection()
    cursor = conn.cursor()
    
    password_hash = hash_password(password)
    
    try:
        cursor.execute(
            "INSERT INTO users (email, name, password_hash) VALUES (%s, %s, %s) RETURNING id",
            (email, name, password_hash)
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
        
        token = create_token(str(user_id), email)
        
        return {
            "user": {"id": str(user_id), "email": email, "name": name},
            "token": token
        }
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")
    finally:
        cursor.close()
        conn.close()

def login_user(email: str, password: str):
    conn = get_neon_connection()
    cursor = conn.cursor()
    
    password_hash = hash_password(password)
    
    cursor.execute(
        "SELECT id, name FROM users WHERE email = %s AND password_hash = %s",
        (email, password_hash)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    user_id, name = result
    token = create_token(str(user_id), email)
    
    return {
        "user": {"id": str(user_id), "email": email, "name": name},
        "token": token
    }
