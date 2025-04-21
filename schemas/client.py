from pydantic import BaseModel
from typing import Optional

class Client(BaseModel):
    id: Optional[str] = None # "client#moscu2"
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

class ClientResponse(Client):
    class Config:
        from_attributes = True 