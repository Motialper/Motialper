#include <stdio.h>
int varibal(int *var_1, int *var_2);



int main(){
	int var_1 = 20;
	int var_2 = 10;
	int varib = varibal( &var_1,  &var_2);
	printf("%d\n",var_1);
	printf("%d\n",var_2);
}


int varibal(int *var_1, int *var_2)
{
	int temp =  *var_1 ;
	*var_1 = (*var_1) * (*var_2);
	*var_2 = temp -  (*var_2);

}






