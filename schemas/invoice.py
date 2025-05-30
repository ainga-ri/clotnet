from typing import Optional
from pydantic import BaseModel, field_validator
from schemas.client import Client
import re
from datetime import date

class Invoice(BaseModel):
    id: Optional[str] = None # "invoice#unique_id"
    client_info: Client
    number: str
    invoice_date: str
    month: str
    deadline: str

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

class InvoiceResponse(Invoice):
    class Config:
        from_attributes = True 