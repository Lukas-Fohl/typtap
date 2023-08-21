buildIt:
	gcc -o ./build/typtap ./src/main.c -std=c99 -O2

run:
	gcc -o ./build/typtap ./src/main.c -std=c99
	./build/typtap