# basic class to handle the CRUD functions

from typing import Optional
from uuid import UUID
from app.schemas.user_schema import UserAuth
from app.models.user_model import User
from app.core.security import get_password, verify_password
import pymongo

from app.schemas.user_schema import UserUpdate


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username=user.username,
            mail=user.mail,
            hashed_password=get_password(user.password)
        )
        await user_in.save()
        return user_in
    
    @staticmethod
    async def authenticate(mail: str, password: str) -> Optional[User]:
        user: User = await UserService.get_user_by_mail(mail=mail)  #prolly an error
        if not user:
            return None
        if not verify_password(password=password, hashed_pass=user.hashed_password):
            return None
        
        return user
    
    @staticmethod
    async def get_user_by_mail(mail: str) -> Optional[User]:
        user = await User.find_one(User.mail == mail)
        return user
    
    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user
    
    @staticmethod
    async def update_user(id: UUID, data: UserUpdate) -> User:
        user = await User.find_one(User.user_id == id)
        if not user:
            raise pymongo.errors.OperationFailure("User not found")
    
        await user.update({"$set": data.dict(exclude_unset=True)})
        return user