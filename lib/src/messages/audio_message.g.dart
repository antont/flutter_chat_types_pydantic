// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'audio_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class AudioMessage(BaseModel):  
    author: User
    createdAt: Optional[int] = None
    duration: Duration
    id: str
    metadata: Optional[dict] = None
    mimeType: Optional[str] = None
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
    waveForm: Optional[list[float]] = None
