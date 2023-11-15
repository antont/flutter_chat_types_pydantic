// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'video_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class VideoMessage(BaseModel):  
    author: User
    createdAt: Optional[int] = None
    height: Optional[float] = None
    id: str
    metadata: Optional[dict] = None
    name: str
    remoteId: Optional[str] = None
    repliedMessage: Optional[Message] = None
    roomId: Optional[str] = None
    showStatus: Optional[bool] = None
    size: float
    status: Optional[Status] = None
    type: Optional[MessageType] = None
    updatedAt: Optional[int] = None
    uri: str
    width: Optional[float] = None
