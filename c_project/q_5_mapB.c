#include <stdio.h>
#include <stdlib.h>



int** create_lists_of_list(int number_of_arrays, int *len_of_arr)
	{
	int **arr;
	
	arr = malloc(sizeof(int*) * number_of_arrays);
	for (int i = 0; i < number_of_arrays; ++i)
	{
		printf("Enter number of elements in list %d: ", i + 1);
		int m;
		scanf("%d",&m);
		*(len_of_arr + i) = m;
		*arr = malloc(sizeof(int) * m); 
		printf("Enter the elements %d: ", i );
		int k;
		for (int j = 0; j < m; ++j)
		{
			scanf("%d", &k);
			*(*arr + j) = k;
		}
	}
	return arr;
	}
void print_arrays(int** arr, int *len_of_arr, int n)
	{
	
	for (int j = 0; j < n; ++j)
		{
		printf("the list number %d is: ",  j);
		for (int i = 0; i < *(len_of_arr + j); i++)
		{
		printf("%d ", *(*(arr + i)+ j));
		}
		printf("\n");
	}
	}
void clean_memory(int** arr, int n)
{
	for (int i = 0; i < number_of_arrays ;i++)
		free(arr);
	for (int j = 0; j < m; i++)
		free(*arr);
}
int main()
{
	printf("Enter number of lists: ");
	int n;
	scanf("%d", &n);
	int* len_of_arr = malloc(sizeof(int) * n);
	int** a = create_lists_of_list(n, len_of_arr);
	print_arrays(a, len_of_arr, n);
	clean_memory(a, n);
	}
