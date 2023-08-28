from enum import Enum

class contentType(Enum):
    header = 1
    text = 2
    bulletpoint =  3
    code = 4
    bold = 5
    none = 6

class linePart:
    linePartContent:str = ""
    linePartType:contentType = contentType.none
    def __init__(self,content_:str,type_:contentType) -> None:
        self.linePartContent = content_
        self.linePartType = type_
        pass

class line:
    lineParts:[linePart] = [linePart]

class file:
    lines:[line] = [line]

fullLineToken = ["$h","$p"]
partLineToken = ["$b"]

def contentTypeFromStr(input: str) -> contentType:
    match str(input):
        case "$h":
            return contentType.header
        case "$p":
            return contentType.bulletpoint
        case "$b":
            return contentType.bold
        case _:
            return contentType.none
