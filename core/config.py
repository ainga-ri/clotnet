from pydantic_settings import BaseSettings
from typing import List

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
    # MONGODB_URL: str = "mongodb://localhost:27017"
    # MONGODB_DB_NAME: str = "invoice_db"
    # MONGODB_USERNAME: str | None = None
    # MONGODB_PASSWORD: str | None = None
    
    class Config:
        case_sensitive = True
        env_file = ".env"

    

settings = Settings() 