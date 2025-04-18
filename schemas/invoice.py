from pydantic import BaseModel

class Invoice(BaseModel):
    invoice_number: int
    invoice_date: str
    service_description: str
    address: str
    month: str
    price_per_hour: str
    total_price: str
    payment_condition: str
    due_date: str
    payment_method: str
    account_number: str
    iban: str
    net_amount: str
    vat: str
    total_amount: str
    nif: str

class InvoiceResponse(Invoice):
    id: str
    file_path: str

    class Config:
        from_attributes = True 