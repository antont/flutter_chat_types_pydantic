// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'image_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class ImageMessage(BaseModel):  
    author: User
    createdAt: Optional[int]
    height: Optional[float]
    id: str
    metadata: Optional[dict]
    name: str
    remoteId: Optional[str]
    repliedMessage: Optional[Message]
    roomId: Optional[str]
    showStatus: Optional[bool]
    size: num
    status: Optional[Status]
    type: Optional[MessageType]
    updatedAt: Optional[int]
    uri: str
    width: Optional[float]
