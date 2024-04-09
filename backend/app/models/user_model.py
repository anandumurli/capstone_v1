from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field
import pymongo

class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: Indexed(str, unique=True) 
    mail: Indexed(str, unique=True)
    hashed_password: str
    first_name: Optional[str] = None 
    last_name: Optional[str] = None
    disabled: Optional[bool] = None

    class Settings:
        name = "users"

    def __repr__(self) -> str:
        return f"<User {self.mail}>"

    def __str__(self) -> str:
        return self.mail

    def __hash__(self) -> int:
        return hash(self.mail)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.mail == other.mail
        return False

    @property
    def create(self) -> datetime:
        return self.id.generation_time
    
    @classmethod
    async def by_email(self, mail: str) -> "User":
        return await self.find_one(self.mail == mail)
    