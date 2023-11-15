#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel

from .preview_data import PreviewData

class PreviewData(BaseModel):  
    description: Optional[str]
    image: Optional[PreviewDataImage]
    link: Optional[str]
    title: Optional[str]

class PreviewDataImage(BaseModel):  
    height: float
    url: str
    width: float

