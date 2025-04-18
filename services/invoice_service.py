import os
import uuid
from core.config import settings
from schemas.invoice import Invoice
from services.pdf_generator import InvoiceData
# from repositories.mongodb import MongoDBRepository



class InvoiceService:
    # def __init__(self, repository: MongoDBRepository):
        # self.repository = repository

    @staticmethod
    async def generate_invoice(invoice_data: Invoice) -> str:
        """
        Generate an invoice PDF and return the file path and unique ID
        """
        # Generate unique filename
        invoice_id = str(uuid.uuid4())
        # filename = f"invoice_{invoice_id}.pdf"
        
        # Create invoice object and generate PDF
        invoice = InvoiceData()

        invoice.create_invoice(invoice_data=invoice_data)
        
        return invoice_id 

    # async def generate_invoice(self, invoice_data: InvoiceCreate) -> tuple[str, bytes]:
    #     """
    #     Generate invoice and store in MongoDB
    #     """
    #     # Generate PDF
    #     pdf_data = self._create_pdf(invoice_data)  # This returns the PDF bytes

    #     # Prepare metadata
    #     metadata = {
    #         "invoice_number": invoice_data.invoice_number,
    #         "invoice_date": invoice_data.invoice_date,
    #         "customer": invoice_data.address,
    #         "amount": invoice_data.total_amount
    #     }

    #     # Store in MongoDB using GridFS
    #     invoice_id = await self.repository.store_invoice_pdf(
    #         str(invoice_data.invoice_number),
    #         pdf_data,
    #         metadata
    #     )

    #     return invoice_id, pdf_data

    async def get_invoice(self, invoice_id: str) -> bytes:
        """
        Retrieve invoice PDF from MongoDB
        """
        return await self.repository.get_invoice_pdf(invoice_id) 