#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from ..message import Message

class PartialFile(BaseModel):  
    metadata: Optional[dict] = None
    mimeType: Optional[str] = None
    name: str
    repliedMessage: Optional[Message] = None
    size: float
    uri: str

