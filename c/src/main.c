#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "./util/util.h"
#include "./pdf/pdf.h"

int main(){
	noteFile mainFile = noteFileContrEmpty();
	
	addLine(&mainFile,
		lineConstr(
			text,
			0,
			"someText more Text"
		)
	);

	line someNewLine = lineConstr(
		header,
		0, 
		"some Header"
	);

	addLine(&mainFile,someNewLine);

	for(int i = 0; i < LINELENGTH; i++){
		printf("%c",(char)(mainFile.lines[0].content[i]));
	}

	printf("\n");
	
	return 0;
}
