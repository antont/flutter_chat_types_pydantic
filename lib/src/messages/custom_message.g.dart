// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'custom_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class CustomMessage(BaseModel):  
    author: User
    createdAt: Optional[int] = None
    id: str
    metadata: Optional[dict] = None
    remoteId: Optional[str] = None
    repliedMessage: Optional[Message] = None
    roomId: Optional[str] = None
    showStatus: Optional[bool] = None
    status: Optional[Status] = None
    type: Optional[MessageType] = None
    updatedAt: Optional[int] = None
