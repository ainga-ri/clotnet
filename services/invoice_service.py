import os
import uuid
from core.config import settings
from models.invoice import DBInvoice
from schemas.invoice import Invoice
from services.pdf_generator import InvoiceData
from typing import List, Optional
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

    async def save_invoice(self, invoice_data: Invoice) -> str:
        """
        Save invoice to MongoDB using Beanie
        """
        # Create a new DBInvoice document
        db_invoice = DBInvoice(
            id=await DBInvoice.generate_id(),
            client_info=invoice_data.client_info,
            number=invoice_data.number,
            invoice_date=invoice_data.invoice_date,
            month=invoice_data.month,
            deadline=invoice_data.deadline
        )
        
        # Insert the document into the database
        await db_invoice.insert()
        print(f"Successfully inserted invoice with ID: {db_invoice.id}")
        
        return db_invoice.id

    async def get_invoice(self, invoice_id: str) -> Optional[DBInvoice]:
        """
        Retrieve invoice from MongoDB by ID
        """
        return await DBInvoice.get(invoice_id)
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