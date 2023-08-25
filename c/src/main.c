#include <stdio.h>
#include <stdlib.h>

#include "./file/file.h"

int main(){
	char* path = "/home/lukas/code/typtap/testFiles/main.file";
	char* test = readFile(path);
	printf("%s\n",test);
	return 0;
}
