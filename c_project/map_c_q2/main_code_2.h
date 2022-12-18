#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define STK_SIZE 4

int push(int val);
int pop();
int calculations();

//int stk_ptr = 0;
int stack[STK_SIZE]; /* stack and stack pointer */
int top_num = -1;  
