#include <stdio.h>
void Hanoi( int n, char a,char b,char c);


int main()
{
	Hanoi( 3,'a','b','c');
}



void Hanoi( int n, char a,char b,char c)
{
	if (n<1){
		printf("no ring ""\n");
			return;
			}
	if (n==1)
		printf("move the ring from %c to %c ""\n", a,c);
	
	else {	
		Hanoi(n-1, a,c,b);
		printf("move the ring from %c to %c ""\n", a,b);
		Hanoi(n-1, b,c,a);

}
		
}

















