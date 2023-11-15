#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from user import User
from message import Message

class TextMessage(BaseModel):  
    author: User
    createdAt: Optional[int]
    id: str
    metadata: Optional[dict]
    previewData: Optional[PreviewData]
    remoteId: Optional[str]
    repliedMessage: Optional[Message]
    roomId: Optional[str]
    showStatus: Optional[bool]
    status: Optional[Status]
    text: str
    type: Optional[MessageType]
    updatedAt: Optional[int]

