#include <stdio.h>
#include <stdlib.h> 	
int creat_tempP();
void swap(int **a, int **b);

int main()
{
	int arr_a[ ] = {5,3,2,6};
	int arr_b[ ] = {6,9,2,5,7,3};
	int* a = arr_a;
	int* b = arr_b;
	swap(&a,&b);
	for (int i = 0; i < 6; i++)
	 	printf("%2d",*(a+i));
	printf("\n");
	
	for (int i = 0; i < 4; i++)
		printf("%2d",*(b+i));

}


void swap(int **a, int **b)
{ 
	int *tmp;
	tmp = *a;
	 *a = *b;
	 *b = tmp;
}








