from datetime import datetime

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
            bill["idCompany"] = str(bill["idCompany"])

            bills.append(bill)

        return bills

    
    async def get_bills_by_month_year_current(self, company_id: str):

        cursor = self.collection.find(
            {
               "idCompany": ObjectId(company_id),
               "mes": datetime.now().month,
               "año": datetime.now().year
            }
        )
       
        bills = []

        async for bill in cursor:

            bill["_id"] = str(bill["_id"])
            bill["idCompany"] = str(bill["idCompany"])

            bills.append(bill)

        return bills
    
    async def get_bills_by_month_year(self, company_id: str, month: int, year: int):

        cursor = self.collection.find(
            {
               "idCompany": ObjectId(company_id),
               "mes": month,
               "año": year
            }
        )
   
        bills = []

        async for bill in cursor:

            bill["_id"] = str(bill["_id"])
            bill["idCompany"] = str(bill["idCompany"])

            bills.append(bill)

        return bills

    async def get_bills_by_year(self,company_id:str,year:int):
       cursor=self.collection.find({
          "idCompany":ObjectId(company_id),
          "año":year
       })

       bills=[]

       async for bill in cursor:
           bill["_id"] = str(bill["_id"])
           bill["idCompany"] = str(bill["idCompany"])

           bills.append(bill)

       return bills   
