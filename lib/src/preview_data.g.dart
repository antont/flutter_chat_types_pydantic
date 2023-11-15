// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'preview_data.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class PreviewData(BaseModel):  
    description: Optional[str] = None
    image: Optional[PreviewDataImage] = None
    link: Optional[str] = None
    title: Optional[str] = None

class PreviewDataImage(BaseModel):  
    height: float
    url: str
    width: float
