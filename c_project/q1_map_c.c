#include <stdio.h>
int isempty();
int isfull();
int pop();
int push(int val);

    int size_of_stack = 8;       
    int stack[8];     
    int top_num = -1;  
int main()
{

   
    push(4);
    push(10);
    push(34);
    push(10);
    push(19);
    push(26);

   printf("Elements: \n");

    
   while(!isempty()) {
      int val= pop();
      printf("%d\n",val);
   }

   

}

int isempty() {

   if(top_num  == -1)
      return 1;
   else
      return 0;
}

int isfull(){
    if (top_num  == size_of_stack)
        return 1;
    else
        return 0;
}
        
int pop() {
   int val;
	
   if(!isempty()) {
      val = stack[top_num];
      top_num = top_num  - 1;   
      return val;
   } else {
      printf("Stack is empty.\n");
   }
}
int push(int val) {

   if(!isfull()) {
      top_num  = top_num  + 1;   
      stack[top_num] = val;
   } else {
      printf(" Stack is full.\n");
   }
}



