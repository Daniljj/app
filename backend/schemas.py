from pydantic import BaseModel
from datetime import datetime

class ChatCreate(BaseModel):
    user_id: int

class MessageCreate(BaseModel):
    chat_id: int
    sender_id: int
    content: str
    created_at: datetime = datetime.utcnow()
