from fastapi import APIRouter, status,HTTPException

from app.schemas.bill import BillCreate
from app.services.bill_service import BillService

router = APIRouter(
    prefix="/bills",
    tags=["Bills"]
)

bill_service = BillService()

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)

def create_bill(bill: BillCreate):
    return {
        "message": "Gasto creado correctamente",
        "data": bill
    }

@router.get("/{company_id}")

@router.get("/{company_id}")
async def get_bills_by_company(company_id: str):

    print("ENTRÓ AL ENDPOINT")
    print("COMPANY ID:", company_id)

    bills = await bill_service.get_bills_by_company(company_id)

    if not bills:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron gastos para esta empresa"
        )

    return bills