from beanie import Document
from datetime import date
from schemas.client import Client
from pydantic import field_validator
import re

class DBInvoice(Document):
    id: str # "invoice#unique_id" # Indexed(str, unique=True)  # Indexed for faster queries
    client_info: Client
    number: str
    invoice_date: str
    month: str
    deadline: str

    class Settings:
        name = "invoices"  # Collection name
        use_state_management = True

    @field_validator('invoice_date', 'deadline')
    @classmethod
    def validate_date_format(cls, v: str) -> str:
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', v):
            raise ValueError('Date must be in dd/mm/yyyy format')
        
        # Validate that the date is actually valid
        try:
            day, month, year = map(int, v.split('/'))
            date(year, month, day)  # This will raise ValueError if date is invalid
        except ValueError:
            raise ValueError('Invalid date')
            
        return v

    @classmethod
    async def generate_id(cls) -> str:
        """Generate a custom ID with invoice# prefix"""
        import uuid
        return f"invoice#{uuid.uuid4()}"