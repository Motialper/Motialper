#include <stdio.h>

int arr_fromUser();

#define NUM_1 2 
#define NUM_2 5 


int main()
{
arr_fromUser();
}



int arr_fromUser()
{
	int i,j ;
	int arr [NUM_1][NUM_2];
	printf(" Enter elements into the Array :n ");
	for (i=0; i< NUM_2; i++	){
		//printf("Enter %2d elements 1: ",i);

		for (int  j=0; j< NUM_1; j++)
			printf("Enter %2d elements and %2d : ",i,j);
			scanf("%d", &arr[i][j]);
		}
}











