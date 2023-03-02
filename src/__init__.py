from dotenv import load_dotenv
from src.logger import logging

logging.info(f"Loading enviroment variable from .env file.")
load_dotenv()