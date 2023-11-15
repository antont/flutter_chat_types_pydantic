#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from user import User
from enum import StrEnum, auto

class Role(StrEnum):
    admin = auto()
    agent = auto()
    moderator = auto()
    user = auto()

class User(BaseModel):  
    createdAt: Optional[int]
    firstName: Optional[str]
    id: str
    imageUrl: Optional[str]
    lastName: Optional[str]
    lastSeen: Optional[int]
    metadata: Optional[dict]
    role: Optional[Role]
    updatedAt: Optional[int]
