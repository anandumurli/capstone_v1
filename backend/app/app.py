from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.user_model import User
from app.api.router import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json"
)

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_init():
    """
        initialize startup services
    """
    
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).capstoneV1
    print(db_client)
    await init_beanie(
        database=db_client,
        document_models= [
            User
        ]
    )

app.include_router(router, prefix=settings.API_STR)