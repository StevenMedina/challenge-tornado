import os

from dotenv import load_dotenv, find_dotenv


load_dotenv()

# Database SQLite
DB_FILE = os.getenv("DB_FILE")
