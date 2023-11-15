#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from user import User
from message import Message

class VideoMessage(BaseModel):  
    author: User
    createdAt: Optional[int]
    height: Optional[float]
    id: str
    metadata: Optional[dict]
    name: str
    remoteId: Optional[str]
    repliedMessage: Optional[Message]
    roomId: Optional[str]
    showStatus: Optional[bool]
    size: num
    status: Optional[Status]
    type: Optional[MessageType]
    updatedAt: Optional[int]
    uri: str
    width: Optional[float]

