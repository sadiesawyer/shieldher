from fastapi import FastAPI
from backend.schemas import Message
from backend.gemini_service import *
from backend.maps_service import resource_search

app = FastAPI() #initialize app

@app.post("/send-message")
async def send_message(message: Message):
    return threat_scan(message.content)

@app.get("/resources-search")
async def get_resources(search_string: str):
    return resource_search(search_string)



