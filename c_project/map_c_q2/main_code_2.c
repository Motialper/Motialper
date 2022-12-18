#include "main_code_2.h"


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