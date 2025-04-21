from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from core.config import settings
from models.invoice import DBInvoice

async def init_db():
    """
    Initialize database connection and Beanie ODM
    """
    # Create Motor client
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    
    # Initialize Beanie with the Product document class
    await init_beanie(
        database=client.invoices,
        document_models=[DBInvoice]
    )
    
    print(f"Connected to MongoDB: {settings.MONGODB_URL}")
    print(f"Database: {settings.MONGODB_DB_NAME}") 