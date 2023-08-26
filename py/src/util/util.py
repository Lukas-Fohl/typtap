from enum import Enum

class contentType(Enum):
    header = 1
    text = 2
    bulletpoint =  3
    code = 4
    none = 5

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

listOfTokens = ["$h","$b"]