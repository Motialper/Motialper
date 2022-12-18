#include "main_code_2.h"
//#include "main_code_2.c"

int main(){

    push(4);
    push(10);
    push(34);
    push(10);
    push(2);

    int len = STK_SIZE - 1;
    char* oper = (char *)malloc(sizeof(char)*(len));
    *(oper) = '+';
    *(oper + 1) = '-';
    *(oper + 2) = '*';
    *(oper + 3) = '/';
    calculations(stack, oper, len);
    free(oper);
}
