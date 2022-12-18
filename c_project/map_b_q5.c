#include <stdio.h>
#include <stdlib.h>
//#include <fraction.h>

struct Node 
{
	int value;
	struct Node* next;
}
;
void insert(struct Node** head, int new_data);
void reverse(struct Node** head);
void printList_L(struct Node* head);
;


int main()
{
	struct Node* head = NULL;
	insert(&head, 4);
	insert(&head, 47);
	insert(&head, 132);
	insert(&head, 26);
	printf("The linked list is:\n");	
	printList_L(head);
	printf("\n");
	printf("The reverse linked list is:\n");
	reverse(&head);
	printList_L(head);

}

void insert(struct Node** head, int new_data)
{
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->value= new_data;
	new_node->next = (*head);
	(*head) = new_node;
}



void reverse(struct Node** head)
{
	struct Node* temp = *head;
	struct Node* prev= NULL;
	struct Node* next = NULL;
	
	while (temp != NULL){
		next = temp-> next;
		temp-> next = prev;
		prev = temp;
		temp = next;
		
		*head = prev;
}
}

void printList_L(struct Node* head)
{
	struct Node* temp = head;
	while (temp != NULL)
	 {
		printf("%d-> ", temp->value);
		temp = temp->next;
	}
}


	




