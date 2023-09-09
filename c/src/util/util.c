#define LINELENGTH 128
#define FILELENGTH 1024

enum lineTypes {header, text, empty};

typedef struct metaData {
    char creator[64];
    long date;
} metaData;

typedef struct line {
    char content[LINELENGTH];
    int indent;
    enum lineTypes type;
    void (*appendConntent)(struct line* self, char* input);
    void (*setContent)(struct line* self, char* input);
    void (*setFont)(struct line* self, char* font);
}line;

typedef struct noteFile {
    line lines[FILELENGTH];
    void (*addLine)(struct noteFile* self, line input);
}noteFile;

//Line - beginning

void setFont(struct line* self, char* font){
    //todo
}

void appendContent(line* self, char* input){
    int lastIndex = 0;
    for(int i = 0; i < LINELENGTH; i++){
        if (self->content[i] != '\0'){
            lastIndex = i;
        }
    }
    int inputSize = sizeof(input)/sizeof(char);

    inputSize = (lastIndex + inputSize <= LINELENGTH)?
        inputSize:
        (LINELENGTH - lastIndex); //cut of the rest

    for(int i = 0; i < inputSize; i++){
        self->content[lastIndex + i] = input[i];
    }
}

void setContent(line* self, char* input){
    for(int i = 0; i < LINELENGTH; i++){
        self->content[i] = '\0';
    }

    int inputSize = sizeof(input)/sizeof(char);
    for(int i = 0; i < inputSize; i++){
        self->content[i] = input[i];
    }
}

line lineConstrEmpty(){
    line temp;

    temp.appendConntent = appendContent;
    temp.setContent = setContent;
    temp.setFont = setFont;

    for(int i = 0; i < LINELENGTH; i++){
        temp.content[i] = '\0';
    }

    temp.type = empty;

    return temp;
}

line lineConstr(enum lineTypes type_, int indent_, char* input){
    line temp = lineConstrEmpty();

    temp.type = type_;

    temp.indent = indent_;

    int inputSize = strlen(input);

    for(int i = 0; i < inputSize; i++){
        temp.content[i] = input[i];
    }

    return temp;
}

//Line - end

//File - geinning

void addLine(noteFile* self, line input){
    for(int i = 0; i < FILELENGTH; i++){
        if(self->lines[i].type == empty && self->lines[i].content[0] == '\0'){
            self->lines[i] = input;
            break;
        }
    }
}

noteFile noteFileContrEmpty(){
    noteFile temp;
    temp.addLine = addLine;

    for(int i = 0; i < FILELENGTH; i++){
        temp.lines[i] = lineConstrEmpty();
    }

    return temp;
}

//File - end