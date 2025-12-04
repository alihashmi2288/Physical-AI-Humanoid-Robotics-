from pydantic import BaseModel
from typing import List, Optional, Dict

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    history: List[Message]

class ChatResponse(BaseModel):
    response: str
    sources: Optional[List[Dict]] = []

class SelectedChatRequest(BaseModel):
    selected_text: str
    user_query: str

class LatestRequest(BaseModel):
    book_section: str

class LatestResponse(BaseModel):
    response: str
    reasoning: str

class IngestRequest(BaseModel):
    text: str
    metadata: Dict

class SignupRequest(BaseModel):
    email: str
    password: str
    name: str

class LoginRequest(BaseModel):
    email: str
    password: str
