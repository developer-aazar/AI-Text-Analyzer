from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.correction_router import router

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=False,
	allow_methods=["GET", "POST", "OPTIONS"],
	allow_headers=["*"],
)
app.include_router(router)
