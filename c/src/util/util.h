#ifndef UTIL
#define UTIL

#include "./util.c"

enum lineTypes;
typedef struct line line;
typedef struct noteFile noteFile;
typedef struct metaData metaData;

line lineConstrEmpty();
line lineConstr(enum lineTypes type_, int indent_, char* input);
noteFile noteFileContrEmpty();

#endif