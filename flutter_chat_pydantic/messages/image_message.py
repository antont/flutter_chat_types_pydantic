#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from ..user import User
from ..message import Message
from ..message import Status
from ..message import MessageType

class ImageMessage(BaseModel):  
    author: User
    createdAt: Optional[int] = None
    height: Optional[float] = None
    id: str
    metadata: Optional[dict] = None
    name: str
    remoteId: Optional[str] = None
    repliedMessage: Optional[Message] = None
    roomId: Optional[str] = None
    showStatus: Optional[bool] = None
    size: float
    status: Optional[Status] = None
    type: Optional[MessageType] = None
    updatedAt: Optional[int] = None
    uri: str
    width: Optional[float] = None

