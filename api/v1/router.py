from fastapi import APIRouter

from api.v1.endpoints import invoice


api_router = APIRouter()
api_router.include_router(invoice.router, prefix="/invoices", tags=["invoices"]) 