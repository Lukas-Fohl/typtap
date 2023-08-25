from enum import Enum

class contentType(Enum):
    header = 1
    text = 2
    bulletpoint =  3
    code = 4

class linePart:
    linePartContent:str
    linePartType:contentType
    def __init__(self,content_:str,type_:contentType) -> None:
        self.linePartContent = content_
        self.linePartType = type_
        pass

class line:
    lineParts:[]

class file:
    lines:[]