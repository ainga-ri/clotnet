# from app.core.config import settings
# from motor.motor_asyncio import AsyncIOMotorClient
# from gridfs import AsyncIOMotorGridFSBucket
# from datetime import datetime

# class MongoDBRepository:
#     def __init__(self):
#         self.client = None
#         self.db = None
#         self.fs = None  # GridFS instance

#     async def connect(self):
#         self.client = AsyncIOMotorClient(settings.MONGODB_URL)
#         self.db = self.client[settings.MONGODB_DB_NAME]
#         self.fs = AsyncIOMotorGridFSBucket(self.db)  # Initialize GridFS

#     async def store_invoice_pdf(self, invoice_id: str, pdf_data: bytes, metadata: dict):
#         """
#         Store PDF using GridFS with metadata
#         """
#         try:
#             # Store the file with metadata
#             file_id = await self.fs.upload_from_stream(
#                 f"invoice_{invoice_id}.pdf",
#                 pdf_data,
#                 metadata={
#                     "invoice_id": invoice_id,
#                     "created_at": datetime.utcnow(),
#                     "type": "invoice_pdf",
#                     **metadata  # Additional metadata like invoice number, date, etc.
#                 }
#             )
#             return str(file_id)
#         except Exception as e:
#             raise Exception(f"Failed to store PDF: {str(e)}")

#     async def get_invoice_pdf(self, invoice_id: str) -> bytes:
#         """
#         Retrieve PDF data using invoice_id
#         """
#         try:
#             # Find the file by metadata
#             cursor = self.fs.find({"metadata.invoice_id": invoice_id})
#             grid_out = await cursor.next()
            
#             # Download the file content
#             pdf_data = await self.fs.download_to_stream(grid_out._id)
#             return pdf_data
#         except Exception as e:
#             raise Exception(f"Failed to retrieve PDF: {str(e)}")

#     async def close(self):
#         if self.client:
#             self.client.close()