#define lineLength 128
#define fileLength 1024

enum lineTypes {header, text, empty};

typedef struct metaData {
    char creator[64];
    long date;
} metaData;

typedef struct line {
    char content[(int)lineLength];
    enum lineTypes type;
    void (*appendConntent)(char* input);
    void (*setConntent)(char* input);
}line;

typedef struct noteFile {
    line lines[(int)fileLength];
    void (*addLine)(line* input);
}noteFile;

void appendContent(char* input){
    //TODO
}

void setContent(char* input){
    //TODO
}

line lineConstrEmpty(){
    line temp;

    temp.appendConntent = appendContent;
    temp.setConntent = setContent;

    for(int i = 0; i < lineLength; i++){
        temp.content[i] = '\0';
    }
    temp.type = empty;
    return temp;
}

line lineConstr(enum lineTypes type, char* input){
    line temp = lineConstrEmpty();
    int inputSize = sizeof(input)/sizeof(char);
    temp.type = type;
    for(int i = 0; i < inputSize; i++){
        temp.content[i] = input[i];
    }
    return temp;
}