// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'file_message.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class FileMessage(BaseModel):  
    author: User
    createdAt: Optional[int]
    id: str
    isLoading: Optional[bool]
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
