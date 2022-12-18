#include <stdio.h>
#include <stdlib.h> 
#include "main_code.c"

struct Node 
{
	int value;
	struct Node* head = NULL;
	struct Node* next;

};
int isempty();
int isfull();
int pop();
int push(int val);
;
