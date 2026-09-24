import datetime

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
async def get_bills_by_company(company_id: str):

    bills = await bill_service.get_bills_by_company(company_id)

    if not bills:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="bills not found for this company with id: " + company_id
        )

    return bills


@router.get("/billsByMonthCurrent/{company_id}")
async def get_bills_by_month_current(company_id: str):

    bills = await bill_service.get_bills_by_month_current(company_id)

    if not bills:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="bills not found for this company with month current"
        )

    return bills

@router.get("/billsByMonthYear/{company_id}")
async def get_bills_by_month_year(company_id: str, month: int, year: int):

    bills = await bill_service.get_bills_by_month_year(company_id, month, year)

    if not bills:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="bills not found for this company with the specified month and year"
        )

    return bills

router.get("billsByYear/{company_id}")
async def get_bills_by_year(company_id:str, year:int):
    bills = await bill_service.get_bills_by_year(company_id, year)

    if not bills:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="bills not found for this company with the specified year"
        )

    return bills