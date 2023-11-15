#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel


class PreviewData(BaseModel):  
    description: Optional[str] = None
    image: Optional[PreviewDataImage] = None
    link: Optional[str] = None
    title: Optional[str] = None

class PreviewDataImage(BaseModel):  
    height: float
    url: str
    width: float

