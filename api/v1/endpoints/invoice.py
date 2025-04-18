from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse, StreamingResponse

from io import BytesIO

# from core.dependencies import get_invoice_service
from schemas.invoice import Invoice
from services.invoice_service import InvoiceService

router = APIRouter()

@router.post("/generate")
async def generate_invoice(
    invoice_data: Invoice,  # JSON automatically converted to InvoiceCreate
    # service: InvoiceService # = Depends(get_invoice_service)  # Automatically injected
):
    service = InvoiceService()
    invoice_id = await service.generate_invoice(invoice_data)
    return {
        "id": invoice_id,
        "message": "Invoice generated successfully"
    }

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