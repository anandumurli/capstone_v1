from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserAuth, UserOut

from app.services.user_service import UserService
from pymongo.errors import DuplicateKeyError
import pymongo
from beanie.exceptions import RevisionIdWasChanged

user_router = APIRouter()

@user_router.post('/signup', summary="Signup a new user", response_model=UserOut)
async def signup(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except (DuplicateKeyError, RevisionIdWasChanged) as e: #might have to split this into two different blocks later
        print("Error has occured")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )