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

# async def get_invoice_service(
#     repository: MongoDBRepository = Depends(get_repository)
# ) -> InvoiceService:
#     """
#     Creates an InvoiceService instance with the repository dependency
#     """
#     # Ensure repository is connected
#     await repository.connect()
#     return InvoiceService(repository=repository) 