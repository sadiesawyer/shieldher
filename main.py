from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from backend.schemas import Message, SignUpRequest, Token
from backend.gemini_service import *
from backend.maps_service import resource_search
from backend.models import User
from passlib.hash import bcrypt
from sqlalchemy import select
from config import SessionLocal, engine, Base, SECRET_KEY
import jwt

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app = FastAPI() #initialize app

@app.post("/send-message") #checking messages for suspicious, harmful, or harrassing content. gemini generates a report
async def send_message(message: Message):
    return threat_scan(message.content)

@app.get("/resources-search") #search for legal resources for cyber stalking near me
async def get_resources(search_string: str):
    return resource_search(search_string)

@app.post("/login")
async def login(email: str, password: str):
    user = authenticate_user(email, password)
    if not user:
        print("Login failed!")
    encoded_jwt = jwt.encode({"sub": email}, SECRET_KEY, algorithm=ALGORITHM)
    token = Token(access_token=encoded_jwt, token_type="bearer")
    return token

def authenticate_user(email: str, password: str) -> bool:
    db = SessionLocal()
    user = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if not user:
        return False
    if not bcrypt.verify(password, user.hashed_password):
        return False
    return user

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

def get_current_user(token: str = Depends(oauth2_scheme)): #dependency function... shout out chat and https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords for this one
    jwt_decoded = jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM)
    email = jwt_decoded.get("sub")
    if email:
        db = SessionLocal()
        user = db.execute(select(User).where(User.email == email))
        return user

@app.get("/who-am-i")
async def get_me():
    return get_current_user()
