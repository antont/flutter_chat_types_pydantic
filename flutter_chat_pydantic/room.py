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
    createdAt: Optional[int]
    id: str
    imageUrl: Optional[str]
    lastMessages: Optional[list[Message]]
    metadata: Optional[dict]
    name: Optional[str]
    type: Optional[RoomType]
    updatedAt: Optional[int]
    users: list[User]

