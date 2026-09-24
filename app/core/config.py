from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")

MONGODB_URL = (
    f"mongodb://{DB_USER}:{DB_PASSWORD}"
    "@cluster0-shard-00-00.b5p91.mongodb.net:27017,"
    "cluster0-shard-00-01.b5p91.mongodb.net:27017,"
    "cluster0-shard-00-02.b5p91.mongodb.net:27017/"
    f"{DATABASE_NAME}"
    "?ssl=true"
    "&replicaSet=atlas-rjqw2o-shard-0"
    "&authSource=admin"
    "&appName=Cluster0"
)