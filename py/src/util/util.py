from enum import Enum

class contentType(Enum):
    header = 1
    text = 2
    bulletpoint =  3
    code = 4
    bold = 5
    pi = 6
    tab = 7
    italic = 8
    none = 9

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

fullLineToken = ["$h"]
partLineTokenParentheses = ["$b","$i"]
partLineTokenSymbol = ["$pi","$t","$p"]

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
        case "$t":
            return contentType.tab
        case "$i":
            return contentType.italic
        case _:
            return contentType.none
