#include <stdio.h>
#include <stdlib.h>

#include "./util/util.h"

int main(){
	noteFile mainFile = noteFileContrEmpty();
	mainFile.addLine(&mainFile,
		lineConstr(
			text, 
			"someText some more Text"
		)
	);
	for(int i = 0; i < LINELENGTH; i++){
		
		printf("%c",(char)(mainFile.lines[0].content[i]));
	}
	printf("\n");
	return 0;
}
