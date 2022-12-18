#include <stdio.h>
#include <stdlib.h>
struct Node 
{
	int value;
	struct Node* next;

};
int isempty();
int isfull();
int pop();
int push(int val);
;
struct Node* head = NULL;
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
}
int push(int val){
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node-> value= val;
    if (head == NULL)
        new_node->next = NULL;
    else 
        new_node->next = head;
    head = new_node;

}
        
    
    


