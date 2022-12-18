//#include "main_code.h"
#include "main.c"



int isempty(){
    if (head == NULL)
        return 1;
    else
        return 0;
}

int isfull(){
    if (head != NULL)
    
        return 1;
    else
        return 0;
}

int pop(){
    if (isempty())
        printf("Stack is empty.\n");
    else{
        struct Node* temp = head;
        int temp_val = head->value;
        head = head->next;
        free(temp);
       	return temp_val; 
    }

int push(int val){
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->value = val;
    if (head == NULL)
        new_node->next = NULL;
    else 
        new_node->next = head;
    head = new_node;    

}
