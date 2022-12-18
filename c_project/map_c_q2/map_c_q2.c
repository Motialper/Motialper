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



int pop(){
    int val;
    val = stack[top_num];
    top_num = top_num - 1;   
    return val;       
}

int push(int val){
      top_num  = top_num  + 1;   
      stack[top_num] = val;
}


int calculations(char* number, char* operators, int size){
    printf("\n");
	int calc = 0;
	for (int i=0 ; i < STK_SIZE  ; ++i)
		{
		int num_1 = pop(number);
		int num_2 = pop(number);
		
		if (*(operators + i) == '+')
			calc = num_1 + num_2;
		
		else if (*(operators + i) == '-')
			calc = num_1 - num_2;
				
		else if (*(operators + i) == '/')
			calc = num_1 / num_2;

		else if (*(operators + i) == '*')
			calc = num_1 * num_2;
			
		printf("->%d\n",calc);	
		push(calc);
		}



}