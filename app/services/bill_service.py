from bson import ObjectId

from app.database.mongodb import database
from app.schemas.bill import BillCreate


class BillService:

    def __init__(self):
        self.collection = database["gastos"]

    async def create_bill(self, bill: BillCreate):

        bill_data = bill.model_dump()

        result = await self.collection.insert_one(bill_data)

        return str(result.inserted_id)

    async def get_bills_by_company(self, company_id: str):

        cursor = self.collection.find(
            {
               "idCompany": ObjectId(company_id)
            }
        )
       
        bills = []

        async for bill in cursor:

            bill["_id"] = str(bill["_id"])
            print(bill)
            bill["idCompany"] = str(bill["idCompany"])

            bills.append(bill)

        return bills