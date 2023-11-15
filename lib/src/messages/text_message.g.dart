// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'text_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class TextMessage(BaseModel):  
    author: User
    createdAt: Optional[int]
    id: str
    metadata: Optional[dict]
    previewData: Optional[PreviewData]
    remoteId: Optional[str]
    repliedMessage: Optional[Message]
    roomId: Optional[str]
    showStatus: Optional[bool]
    status: Optional[Status]
    text: str
    type: Optional[MessageType]
    updatedAt: Optional[int]
