from fastapi import APIRouter

from app.database.mongodb import database


router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
async def health_check():
    return {
        "status": "API funcionando correctamente"
    }


@router.get("/database")
async def database_test():
    try:
        await database.command("ping")

        return {
            "status": "success",
            "message": "MongoDB conectado correctamente"
        }

    except Exception as error:
        return {
            "status": "error",
            "message": str(error)
        }