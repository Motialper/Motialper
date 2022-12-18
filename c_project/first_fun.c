#include <stdio.h>
#define ARRAY_SIZE 6

int sort(int Array[ARRAY_SIZE]);

int main()
{

	int i, Array[ARRAY_SIZE];
	printf(" Enter elements into the Array :n ");
	for (i=0; i< ARRAY_SIZE ; i++	)
		{
		printf("Enter %2d elements : ",i);
		scanf("%d",&Array[i]);
		}
	
	sort(Array);
	printf(" here is the new Array : n ");
	for (i=0; i< ARRAY_SIZE ; i++)
	{
	printf("%3d",Array[i]);
	}
	return 0;


}

int sort(int Array[ARRAY_SIZE])
{
	for(int i = 1; i < ARRAY_SIZE; i++)
	{
	    int k = Array[i];
	    int j= i - 1;

	    while (j>=0 && Array[j] > k )
	    {
		Array[j + 1] = Array[j];
		j--;
		
	    }
	    Array[j + 1] = k;	    
	    
	    
	}
}
