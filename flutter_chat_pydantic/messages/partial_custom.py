#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from ..message import Message

class PartialCustom(BaseModel):  
    metadata: Optional[dict] = None
    repliedMessage: Optional[Message] = None

