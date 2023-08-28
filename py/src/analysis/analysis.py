from util import util as util

def splitContent(content:str)->util.file:
    listOfLines = content.split('\n')
    tempFileReturn = util.file()

    for currentLine in listOfLines:
        tempLine = util.line()
        tempLinePart = util.linePart("",util.contentType.none)

        #find full line token
        for lineToken in util.fullLineToken:
            if len(str(currentLine)) >= len(str(lineToken)):
                if lineToken in currentLine:
                    tempLinePart = util.linePart(str(currentLine),util.contentTypeFromStr(lineToken))
                    break
        tempLine.lineParts.append(tempLinePart)

        #find part line token

        #split lines if necessary
        #--> get content type
        #combine
        pass
    return tempFileReturn