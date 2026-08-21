from fastapi import APIRouter, status

from app.schemas.bill import BillCreate


router = APIRouter(
    prefix="/bills",
    tags=["Bills"]
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)

def create_bill(bill: BillCreate):
    return {
        "message": "Gasto creado correctamente",
        "data": bill
    }