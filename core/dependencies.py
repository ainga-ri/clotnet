# from fastapi import Depends
# from app.repositories.mongodb import MongoDBRepository
# from app.services.invoice_service import InvoiceService

# async def get_repository():
#     repo = MongoDBRepository()
#     await repo.connect()
#     try:
#         yield repo
#     finally:
#         await repo.close()

from fastapi import Depends
from services.invoice_service import InvoiceService

async def get_invoice_service() -> InvoiceService:
    """
    Creates an InvoiceService instance
    """
    return InvoiceService() 