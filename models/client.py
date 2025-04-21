from typing import List
from beanie import Document
from datetime import date
from models.invoice import DBInvoice
from schemas.client import Client

class DBClient(Document):
    id: str # # What is Indexed? "client#moscu2"
    displayed_title: str 
    client: str
    street: str
    zip_code_city: str
    cif: str
    description: str
    description_street: str
    total_price_description: float
    net_price: float
    vat21: float
    total_price: float
    condition: str
    payment_method: str
    account_number: str
    iban: str

    class Settings:
        name = "clients"

    @classmethod
    async def generate_id(cls) -> str:
        import uuid
        return f"client#{uuid.uuid4()}"