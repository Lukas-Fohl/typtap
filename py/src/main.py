from file import file as file
from analysis import analysis as analysis
from graphic import graphic as graphic


def main():

    """
    fileContent = file.readFile("../testFiles/main.file")
    printing(3,0,fileContent)
    printing(3,1,fileContent)
    printing(3,2,fileContent)
    printing(3,3,fileContent)
    printing(3,4,fileContent)
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

def printing(line,index,fileContent)->None:
    print("T line: " + str(line) + " ; index: " + str(index) + str(" ") + str(analysis.splitContent(fileContent).lines[line].lineParts[index].linePartType))
    print("C line: " + str(line) + " ; index: " + str(index) + str(" ") + str(analysis.splitContent(fileContent).lines[line].lineParts[index].linePartContent))
    pass

if __name__ == "__main__":
    main()