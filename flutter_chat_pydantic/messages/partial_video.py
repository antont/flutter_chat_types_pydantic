#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from message import Message

class PartialVideo(BaseModel):  
    height: Optional[float]
    metadata: Optional[dict]
    name: str
    repliedMessage: Optional[Message]
    size: num
    uri: str
    width: Optional[float]

