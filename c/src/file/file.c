#include <stdio.h>

char* readFile(char* filePath){ 
    FILE* file;

    file = fopen(filePath, "r");
 
    if (NULL == file) {
        printf("file can't be opened \n");
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    char* fileContent = (char*)malloc(file_size + 1);

    if (fileContent == NULL) {
        perror("Memory allocation error");
        fclose(file);
    }
    fread(fileContent, 1, file_size, file);

    fileContent[file_size] = '\0';

    fclose(file);

    return fileContent;
}
