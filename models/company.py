from beanie import Document, Indexed
from typing import Optional

class DBCompany(Document):
    id: str = Indexed(unique=True)  # Fixed syntax for Indexed
    address: str
    zip_code_city: str
    telephone: str
    email: str
    boss: str
    nif: str

    class Settings:
        name = "companies"  # Collection name
        use_state_management = True
        indexes = [
            "id",  # Index on id field
            [("id", 1)],  # Compound index if needed
        ]

    @classmethod
    async def generate_id(cls) -> str:
        """Generate a custom ID with company# prefix"""
        import uuid
        return f"company#{uuid.uuid4()}"

    @classmethod
    async def find_by_prefix(cls, prefix: str):
        """Find all companies with IDs starting with the given prefix"""
        return await cls.find({"id": {"$regex": f"^{prefix}"}})