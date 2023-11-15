import flutter_chat_pydantic
from flutter_chat_pydantic.user import User
from flutter_chat_pydantic.message import Message

def test_imports():
    print(flutter_chat_pydantic)
    print(Message)

def test_create_user():
    user = User(
        id = "tester"
    )
    return user

def test_create_message():
    user = test_create_user()
    message = Message(
        author=user,
        createdAt=1,
        id="test message x"
    )
    print(message)
