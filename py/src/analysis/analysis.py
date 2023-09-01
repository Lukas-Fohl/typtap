from util import util as util

def splitContent(content:str)->util.file:
    listOfLines = content.split('\n')
    tempFileReturn = util.file()

    for currentLine in listOfLines:
        tempLine = util.line()

        #find full line token [done]
        wordsFullLine = currentLine.split(' ')
        for lineToken in util.fullLineToken:
            for word in wordsFullLine: 
                #if len(str(currentLine)) >= len(str(lineToken)):
                #if (lineToken == currentLine) and ( not ( ("\\" + str(lineToken)) in currentLine ) ):
                if (lineToken == word):
                    tempLine.lineParts.append(util.linePart(str(currentLine),util.contentTypeFromStr(lineToken)))
                    break
        #to not add any other tokens to the header
        if len(tempLine.lineParts) > 0:
            tempFileReturn.lines.append(tempLine)
            continue

        #TODO merge partLine & parentheses

        wordsPart = currentLine.split(' ')
        for i in range(len(wordsPart)):
            for partLineToken in util.partLineTokenSymbol:
                if wordsPart[i] == str(partLineToken):
                    tempLine.lineParts.append(util.linePart(str(""),util.contentTypeFromStr(str(partLineToken))))
                else:
                    tempLine.lineParts.append(util.linePart(str(str(wordsPart[i]) + " "),util.contentType.text))


        wordsPartParentheses = currentLine.split(' ')
        currentContentType = util.contentType.text
        for i in range(len(wordsPartParentheses)):
            for partLineToken in util.partLineTokenParentheses:
                if str(partLineToken) == wordsPartParentheses[i]:
                    if currentContentType == partLineToken:
                        currentContentType = util.contentType.text
                    else:
                        currentContentType = partLineToken
            if not wordsPartParentheses[i] in util.partLineTokenParentheses:
                tempLine.lineParts.append(util.linePart(str(wordsPartParentheses[i] + " "),currentContentType))

        #find normale line [done]
        if len(tempLine.lineParts) == 0:
            tempLine.lineParts.append(util.linePart(str(currentLine),util.contentType.text))

        tempFileReturn.lines.append(tempLine)
    return tempFileReturn