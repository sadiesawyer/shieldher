from pydantic import BaseModel 

class Message(BaseModel): #https://fastapi.tiangolo.com/tutorial/body/
    content: str #using pydantic because not i'm storing this data




