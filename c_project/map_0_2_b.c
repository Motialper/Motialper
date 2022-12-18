#include <stdio.h>

int findOut_the_midel(char s[]);

int main(){
	char  s	[] = "a-z";
	findOut_the_midel(s);
	return 0;
}




int findOut_the_midel(char s[])
{
	int head = s[0];
	int end = s[2];
	for (int i = head; i < end; i++)
	{
		printf("%2c", i);
		//printf("\n");
	
	
	}


}


















