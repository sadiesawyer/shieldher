from fastapi import FastAPI
from backend.schemas import Message, SignUpRequest
from backend.gemini_service import *
from backend.maps_service import resource_search
from backend.models import User
from passlib.hash import bcrypt
from sqlalchemy import select
from config import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI() #initialize app

@app.post("/send-message") #checking messages for suspicious, harmful, or harrassing content. gemini generates a report
async def send_message(message: Message):
    return threat_scan(message.content)

@app.get("/resources-search") #search for legal resources for cyber stalking near me
async def get_resources(search_string: str):
    return resource_search(search_string)

@app.post("/login")
async def login(email: str, password: str):
    db = SessionLocal()
    user = db.execute(select(User).where(User.email == email))
    bcrypt.verify(password, user.hashed_password)
    #issue a token here

@app.post("/sign-up")
async def sign_up(signup: SignUpRequest):
    db = SessionLocal()
    if (signup.password != signup.password2):
        print("Passwords don't match.")
    encrypted_pass = bcrypt.hash(signup.password)
    new_user = User(email=signup.email, hashed_password=encrypted_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

