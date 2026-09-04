from fastapi import FastAPI
from api.routers.correction_router import router

app = FastAPI()
app.include_router(router)
