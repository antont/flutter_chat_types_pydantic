"""failed to conf the Dart Builder all the way, so cleaning up here"""
import os

DIR = "lib/src"
OUT = "flutter_chat_pydantic"

type2module = {
    'User': 'user',
    'Message': 'message',
    'Status': 'message',
    'MessageType': 'message',
    'PreviewData': 'preview_data'
}

enums = {
    'class Room': """class RoomType(StrEnum):
    channel = auto()
    direct = auto()
    group = auto()
""",
    'class User': """class Role(StrEnum):
    admin = auto()
    agent = auto()
    moderator = auto()
    user = auto()
"""
}

def process(content: str, dirpath: str, file_name: str):
    begin_py = content.index('class')
    content = content[begin_py:]

    imports = ""
    for type, module in type2module.items():
        if file_name.split('.')[0] == module:
            continue
        if type in content:
            if dirpath.endswith('/src'):
                relimport = '.'
            elif dirpath.endswith('src/messages'):
                relimport = '..'
            else:
                raise RuntimeError(f"Unknown dirpath {dirpath}")
            imports = "\n".join(
                [imports,
                f"from {relimport}{module} import {type}"]
            )

    inject_enums = ""
    for k, v in enums.items():
        if k in content:
            inject_enums = "".join([inject_enums, v])
    if inject_enums:
        inject_enums = "\n".join([f"from enum import StrEnum, auto\n", inject_enums])

    return f"""#AUTOGENERATED from flutter_chat_types_pydantic with pydantic_serializable & post_process.py
from typing import Optional

from pydantic import BaseModel
{imports}
{inject_enums}
{content}
"""

for dirpath, dirnames, filenames in os.walk(DIR):
    print(f"Found directory: {dirpath}")
    for file_name in filenames:
        if file_name.endswith('.g.dart'):
            print(file_name)
            with open(os.path.join(dirpath, file_name), 'r') as file:
                content = file.read()
                processed = process(content, dirpath, file_name)
                out_dir = os.path.join(OUT, os.path.relpath(dirpath, DIR))
                os.makedirs(out_dir, exist_ok=True)
                file_name_py = file_name.replace('.g.dart', '.py')
                with open(os.path.join(out_dir, file_name_py), 'w') as file:
                    file.write(processed)

