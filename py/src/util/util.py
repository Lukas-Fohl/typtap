from enum import Enum

class contentType(Enum):
    header = 1
    text = 2
    bulletpoint =  3
    code = 4
    bold = 5
    pi = 6
    none = 7

class linePart:
    linePartContent:str = ""
    linePartType:contentType = contentType.none
    def __init__(self,content_:str,type_:contentType) -> None:
        self.linePartContent = content_
        self.linePartType = type_
        pass

class line:
    lineParts = []
    def __init__(self) -> None:
        self.lineParts = [linePart]
        self.lineParts.clear()
        pass

class file:
    lines = []
    def __init__(self) -> None:
        self.lines = [line]
        self.lines.clear()
        pass

fullLineToken = ["$h","$p"]
partLineTokenParentheses = ["$b"]
partLineTokenSymbol = ["$pi"]

def contentTypeFromStr(input: str) -> contentType:
    match str(input):
        case "$h":
            return contentType.header
        case "$p":
            return contentType.bulletpoint
        case "$b":
            return contentType.bold
        case "$pi":
            return contentType.pi
        case _:
            return contentType.none
