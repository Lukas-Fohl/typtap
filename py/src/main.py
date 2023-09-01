from file import file as file
from analysis import analysis as analysis
from graphic import graphic as graphic


def main():

    """
    fileContent = file.readFile("../testFiles/main.file")
    #print(fileContent)
    #print(analysis.splitContent(fileContent).lines[3].lineParts[2].linePartType)
    line = 3
    index = 1
    print("T line: " + str(line) + " ; index: " + str(index) + str(" ") + str(analysis.splitContent(fileContent).lines[line].lineParts[index].linePartType))
    print("C line: " + str(line) + " ; index: " + str(index) + str(" ") + str(analysis.splitContent(fileContent).lines[line].lineParts[index].linePartContent))
    """
    #make tokens

    #read file
    #analysis
    #change tokens
    #window
    #export

    startGraphics()

    pass

def startGraphics():
    screen = graphic.init()

    while(True):

        fileContent = file.readFile("../testFiles/main.file")

        #print(analysis.splitContent(fileContent).lines[0].lineParts[0].linePartType)

        if not graphic.update(screen, analysis.splitContent(fileContent)):
            break
    return

if __name__ == "__main__":
    main()