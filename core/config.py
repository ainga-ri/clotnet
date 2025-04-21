from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Invoice Generator API"
    PROJECT_DESCRIPTION: str = "API to generate PDF invoices"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = ["*"]
    
    # File Storage
    UPLOAD_DIR: str = "app/uploads"
    TEMP_DIR: str = "temp"
    
    # MongoDB Configuration
    MONGODB_URL: str
    MONGODB_DB_NAME: str = "invoices"
    
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

    

settings = Settings() 