import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    WORKING_DIRECTORY = os.environ.get('WORKING_DIRECTORY')
    MAX_ITERS = int(os.environ.get('MAX_ITERS', 20))