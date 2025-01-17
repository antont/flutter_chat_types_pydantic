#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from .user import User
from .message import Message
from enum import StrEnum, auto

class RoomType(StrEnum):
    channel = auto()
    direct = auto()
    group = auto()

class Room(BaseModel):  
    createdAt: Optional[int] = None
    id: str
    imageUrl: Optional[str] = None
    lastMessages: Optional[list[Message]] = None
    metadata: Optional[dict] = None
    name: Optional[str] = None
    type: Optional[RoomType] = None
    updatedAt: Optional[int] = None
    users: list[User]

