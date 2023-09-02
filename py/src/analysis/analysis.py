from util import util as util

def splitContent(content:str)->util.file:
    listOfLines = content.split('\n')
    tempFileReturn = util.file()

    for currentLine in listOfLines:
        tempLine = util.line()

        wordsFullLine = currentLine.split(' ')
        for word in wordsFullLine:
            if word in util.fullLineToken:

                #remove token from string
                for i in range(len(wordsFullLine)):
                    if i < len(wordsFullLine):
                        if wordsFullLine[i] in util.fullLineToken:
                            wordsFullLine.pop(i)

                #add to list
                tempLine.lineParts.append(util.linePart(str(' '.join(wordsFullLine)),util.contentTypeFromStr(word)))
                break

        #break
        if len(tempLine.lineParts) > 0:
            tempFileReturn.lines.append(tempLine)
            continue

        words = currentLine.split(' ')
        currentContentType = util.contentType.text
        for i in range(len(words)):
            if words[i] in util.partLineTokenSymbol:
                tempLine.lineParts.append(util.linePart(str(words[i] + " "),util.contentTypeFromStr(words[i])))
            elif words[i] in util.partLineTokenParentheses:
                if currentContentType == util.contentTypeFromStr(words[i]):

                    #to not add the token
                    #tempLine.lineParts.append(util.linePart(str(words[i] + " "),currentContentType))

                    currentContentType = util.contentType.text
                    continue
                else:
                    currentContentType = util.contentTypeFromStr(words[i])
                    continue
                    #continue to not add token

                #tempLine.lineParts.append(util.linePart(str(words[i] + " "),currentContentType))
            elif currentContentType == util.contentType.text:
                tempLine.lineParts.append(util.linePart(str(words[i] + " "),util.contentType.text))
            else:
                tempLine.lineParts.append(util.linePart(str(words[i] + " "),currentContentType))

        if len(tempLine.lineParts) == 0:
            tempLine.lineParts.append(util.linePart(str(currentLine),util.contentType.text))

        tempFileReturn.lines.append(tempLine)
    return tempFileReturn