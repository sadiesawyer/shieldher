from pydantic import BaseModel 

class Message(BaseModel): #https://fastapi.tiangolo.com/tutorial/body/
    content: str #using pydantic because not i'm storing this data

class MessageAnalysis(BaseModel): #schema for api response
    risk_score: str
    explanation: str
    recommended_action: str

class PlaceResult(BaseModel): #schema for places in resources search
    name: str
    address: str
    place_id: str
    website: str

class SignUpRequest(BaseModel):
    email: str
    password: str
    password2: str




