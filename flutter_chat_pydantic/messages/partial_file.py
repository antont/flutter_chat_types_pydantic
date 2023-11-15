#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from message import Message

class PartialFile(BaseModel):  
    metadata: Optional[dict]
    mimeType: Optional[str]
    name: str
    repliedMessage: Optional[Message]
    size: num
    uri: str

