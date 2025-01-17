#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from enum import StrEnum, auto

class Role(StrEnum):
    admin = auto()
    agent = auto()
    moderator = auto()
    user = auto()

class User(BaseModel):  
    createdAt: Optional[int] = None
    firstName: Optional[str] = None
    id: str
    imageUrl: Optional[str] = None
    lastName: Optional[str] = None
    lastSeen: Optional[int] = None
    metadata: Optional[dict] = None
    role: Optional[Role] = None
    updatedAt: Optional[int] = None

