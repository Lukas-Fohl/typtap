from util import util as util

def splitContent(content:str)->util.file:
    listOfLines = content.split('\n');
    tempFileReturn = util.file()
    for i in listOfLines:
        for charOfLine in i:
            pass
        tempLine = util.line()
        tempLinePart = util.linePart("",util.contentType.none)
        tempLine.lineParts.append(tempLinePart)
        #split lines if necessary
        #--> get content type
        #combine
        pass
    return tempFileReturn