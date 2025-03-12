from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Base, Chat, Message
from database import SessionLocal, engine
from schemas import ChatCreate, MessageCreate
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/chats/")
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    db_chat = Chat(**chat.dict())
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

@app.get("/chats/{user_id}")
def get_user_chats(user_id: int, db: Session = Depends(get_db)):
    return db.query(Chat).filter(Chat.user_id == user_id).all()

@app.post("/messages/")
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    db_message = Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/messages/{chat_id}")
def get_chat_messages(chat_id: int, db: Session = Depends(get_db)):
    return db.query(Message).filter(Message.chat_id == chat_id).all()

@app.get("/")
def read_root():
    return {"status": "API is working"}
