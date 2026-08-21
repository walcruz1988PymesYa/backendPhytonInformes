from datetime import date, datetime
from sqlite3 import Date
from pydantic import BaseModel, Field,model_validator


class BillCreate(BaseModel):
    # Greater than or equal (ge) Mayor o igual que 
    # Field() validan un campo individual.

    year: int = Field(..., description="Año del gasto", ge=2000)

    date: Date = Field(..., description="Fecha del gasto")

    description: str = Field(
        ...,
        min_length=1,
        description="Descripción del gasto"
    )

    cash: float | None = Field(
        default=None,
        ge=0,
        description="Monto pagado en efectivo"
    )

    transfer: float | None = Field(
        default=None,
        ge=0,
        description="Monto pagado por transferencia"
    )

    card: float | None = Field(
        default=None,
        ge=0,
        description="Monto pagado con tarjeta"
    )

    category_expense: str = Field(
        ...,
        description="Categoría del gasto"
    )

    value: float = Field(
        ...,
        gt=0,
        description="Valor total del gasto"
    )

    month: int = Field(
        ...,
        ge=1,
        le=12,
        description="Mes del gasto"
    )

    expense_type: str = Field(
        ...,
        description="Tipo de gasto"
    )

    company_id: str = Field(
        ...,
        description="ID de la empresa"
    )

    @model_validator(mode="after")
    def validate_payment_total(self):

        cash = self.cash or 0
        transfer = self.transfer or 0
        card = self.card or 0

        total_payments = cash + transfer + card

        if total_payments != self.value:
            raise ValueError(
                "La suma de los medios de pago debe ser igual al valor total del gasto"
            )

        return self