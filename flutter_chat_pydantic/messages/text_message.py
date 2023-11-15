#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from ..user import User
from ..message import Message
from ..message import Status
from ..message import MessageType
from ..preview_data import PreviewData

class TextMessage(BaseModel):  
    author: User
    createdAt: Optional[int] = None
    id: str
    metadata: Optional[dict] = None
    previewData: Optional[PreviewData] = None
    remoteId: Optional[str] = None
    repliedMessage: Optional[Message] = None
    roomId: Optional[str] = None
    showStatus: Optional[bool] = None
    status: Optional[Status] = None
    text: str
    type: Optional[MessageType] = None
    updatedAt: Optional[int] = None

