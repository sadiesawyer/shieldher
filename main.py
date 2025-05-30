from fastapi import FastAPI
from backend.schemas import Message
from backend.gemini_service import *

app = FastAPI() #initialize app

@app.post("/send-message")
async def send_message(message: Message):
    return threat_scan(message)


