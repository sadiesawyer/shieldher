from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MAPS_API_KEY = os.getenv("MAPS_API_KEY")

