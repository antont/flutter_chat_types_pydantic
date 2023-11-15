// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'file_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class FileMessage(BaseModel):  
    author: User
    createdAt: Optional[int] = None
    id: str
    isLoading: Optional[bool] = None
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
