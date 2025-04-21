from pydantic import BaseModel

class Company(BaseModel):
    address: str
    zip_code_city: str
    telephone: str
    email: str
    boss: str
    nif: str

class CompanyResponse(Company):
    id: str

    class Config:
        from_attributes = True 