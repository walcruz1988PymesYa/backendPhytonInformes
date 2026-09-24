from pymongo import AsyncMongoClient
from app.core.config import MONGODB_URL, DATABASE_NAME

# crea la conexión con tu servidor/cluster de MongoDB.
client = AsyncMongoClient(MONGODB_URL)

# selecciona específicamente la base de datos donde vas a trabajar.
database = client[DATABASE_NAME]