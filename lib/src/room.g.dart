// #GENERATED CODE - DO NOT MODIFY BY HAND

part of 'room.dart';

// **************************************************************************
// PydanticSerializableGenerator
// **************************************************************************

class Room(BaseModel):  
    createdAt: Optional[int]
    id: str
    imageUrl: Optional[str]
    lastMessages: Optional[list[Message]]
    metadata: Optional[dict]
    name: Optional[str]
    type: Optional[RoomType]
    updatedAt: Optional[int]
    users: list[User]
