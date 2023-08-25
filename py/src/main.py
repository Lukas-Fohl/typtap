from file import file as file
from analysis import analysis as analysis


def main():

    fileContent = file.readFile("../testFiles/main.file")

    analysis.splitContent(fileContent)

    #make tokens

    #read file
    #analysis
    #change tokens
    #window
    #export

    return

if __name__ == "__main__":
    main()