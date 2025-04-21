from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse, StreamingResponse
from typing import List

from io import BytesIO

from schemas.invoice import Invoice
from services.invoice_service import InvoiceService
from core.dependencies import get_invoice_service

router = APIRouter()

@router.post("/generate")
async def generate_invoice(
    invoice_data: Invoice,  # JSON automatically converted to Invoice
    service: InvoiceService = Depends(get_invoice_service)
):
    invoice_id = await service.generate_invoice(invoice_data)
    await service.save_invoice(invoice_data)
    return {
        "id": invoice_id,
        "message": "Invoice generated and saved successfully"
    }

@router.get("/{invoice_id}")
async def get_invoice(
    invoice_id: str,
    service: InvoiceService = Depends(get_invoice_service)
):
    invoice = await service.get_invoice(invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

# @router.get("/download/{invoice_id}")
# async def download_invoice(
#     invoice_id: str,
#     service: InvoiceService = Depends(get_invoice_service)
# ):
#     pdf_data = await service.get_invoice(invoice_id)
    
#     return StreamingResponse(
#         BytesIO(pdf_data),
#         media_type="application/pdf",
#         headers={
#             "Content-Disposition": f"attachment; filename=invoice_{invoice_id}.pdf"
#         }
#     )