from fastapi import FastAPI

from app.routers.bills import router as bills_router
from app.routers.health import router as health_router


app = FastAPI(
    title="Sistema PY Backend",
    version="1.0.0"
)



app.include_router(bills_router)
app.include_router(health_router)