// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'audio_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class AudioMessage(BaseModel):  
    author: User
    createdAt: Optional[int]
    duration: Duration
    id: str
    metadata: Optional[dict]
    mimeType: Optional[str]
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
    waveForm: Optional[list[float]]
