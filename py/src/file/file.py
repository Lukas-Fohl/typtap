def readFile(path:str) -> str:
    return open(path).read()

def writeFile(path:str,content:str):
    file = open(path)
    file.write(content)
    pass