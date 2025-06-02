from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_imageattach.entity import Image, image_attachment
import datetime
from config import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Incident(Base):
    __tablename__ = 'incidents'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    timestamp = Column(datetime.datetime)
    incident_date = Column(datetime.date)

    title = Column(String)
    platform = Column(String, nullable=True)
    perpetrator = Column(String, nullable=True)
    message_content = Column(String, nullable = True)
    screenshot_url = image_attachment('Incident_Image')
    location = Column(String, nullable=True)
    report_notes = Column(String)

class Incident_Image(Base, Image):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    incident_id = Column(Integer, ForeignKey('incidents.id'), primary_key=True)





