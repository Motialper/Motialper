#include "main_code.h"
//#include "main_code.c"


int main()
{

    push(5);
    push(30);
    push(24);
    push(260);
    push(194);
    push(26);
	pop(head);
    printf("Elements: \n");

    
    while(!isempty()) {
      int val= pop();
      printf("%d->",val);
	}

}
