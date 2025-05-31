from fastapi import FastAPI
from backend.schemas import Message
from backend.gemini_service import *
from backend.maps_service import resource_search

app = FastAPI() #initialize app

@app.post("/send-message") #checking messages for suspicious, harmful, or harrassing content. gemini generates a report
async def send_message(message: Message):
    return threat_scan(message.content)

@app.get("/resources-search") #search for legal resources for cyber stalking near me
async def get_resources(search_string: str):
    return resource_search(search_string)



