// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'text_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class TextMessage(BaseModel):  
    author: User
    createdAt: Optional[int] = None
    id: str
    metadata: Optional[dict] = None
    previewData: Optional[PreviewData] = None
    remoteId: Optional[str] = None
    repliedMessage: Optional[Message] = None
    roomId: Optional[str] = None
    showStatus: Optional[bool] = None
    status: Optional[Status] = None
    text: str
    type: Optional[MessageType] = None
    updatedAt: Optional[int] = None
