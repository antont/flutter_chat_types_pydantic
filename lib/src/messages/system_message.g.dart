// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'system_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class SystemMessage(BaseModel):  
    author: Optional[User] = None
    createdAt: Optional[int] = None
    id: str
    metadata: Optional[dict] = None
    remoteId: Optional[str] = None
    repliedMessage: Optional[Message] = None
    roomId: Optional[str] = None
    showStatus: Optional[bool] = None
    status: Optional[Status] = None
    text: str
    type: Optional[MessageType] = None
    updatedAt: Optional[int] = None
