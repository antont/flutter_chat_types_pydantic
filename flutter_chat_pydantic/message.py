from enum import StrEnum, auto
from typing import Optional

from pydantic import BaseModel

class MessageType(StrEnum):
    audio = auto()
    custom = auto()
    file = auto()
    image = auto()
    system = auto()
    text = auto()
    unsupported = auto()
    video = auto()

class Status(StrEnum):
    delivered = auto()
    error = auto()
    seen = auto()
    sending = auto()
    sent = auto()

class Message(BaseModel):
    author: "User"
    createdAt: Optional[int] = None
    id: str
    metadata: Optional[dict] = None
    remoteId: Optional[str] = None
    repliedMessage: Optional["Message"] = None
    roomId: Optional[str] = None
    showStatus: Optional[bool] = None
    status: Optional[Status] = None
    updatedAt: Optional[int] = None
