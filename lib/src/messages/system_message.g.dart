// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'system_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class SystemMessage(BaseModel):  
    author: Optional[User]
    createdAt: Optional[int]
    id: str
    metadata: Optional[dict]
    remoteId: Optional[str]
    repliedMessage: Optional[Message]
    roomId: Optional[str]
    showStatus: Optional[bool]
    status: Optional[Status]
    text: str
    type: Optional[MessageType]
    updatedAt: Optional[int]
