// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'preview_data.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class PreviewData(BaseModel):  
    description: Optional[str]
    image: Optional[PreviewDataImage]
    link: Optional[str]
    title: Optional[str]

class PreviewDataImage(BaseModel):  
    height: float
    url: str
    width: float
