from fastapi import APIRouter
from app.api.handlers import user
# from app.api.api_v1.handlers import todo
from app.api.auth.jwt import auth_router
from app.api.general.genesis import gen_router

router = APIRouter()

router.include_router(user.user_router, prefix='/users', tags=["users"])
router.include_router(auth_router, prefix='/auth', tags=["auth"])
router.include_router(gen_router, prefix='/gen', tags=["general"])

# Making a router to handle all the other routers we will eventually create for different models