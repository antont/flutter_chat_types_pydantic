// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'room.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class Room(BaseModel):  
    createdAt: Optional[int] = None
    id: str
    imageUrl: Optional[str] = None
    lastMessages: Optional[list[Message]] = None
    metadata: Optional[dict] = None
    name: Optional[str] = None
    type: Optional[RoomType] = None
    updatedAt: Optional[int] = None
    users: list[User]
