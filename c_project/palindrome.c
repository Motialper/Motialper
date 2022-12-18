#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
int find_error_inPalindrome(char str[], int n, int startFrom);

int main()
{
	
	char str[] = "@@MadAm@$!";
	int n = sizeof(str);
	int startFrom = 0;
	
	for (int i = startFrom; i < n; i++)
		str[i] = tolower(str[i]);
	
	int checkIfPalindrome = find_error_inPalindrome(str,n,startFrom);
	printf("%d\n", checkIfPalindrome );
	return 0;
}





int find_error_inPalindrome(char str[], int n, int startFrom)
{
	int checkIfPalindrome = 1;

	if ((checkIfPalindrome) && (n != startFrom)){
		if (str[startFrom] == str[n])
			checkIfPalindrome = find_error_inPalindrome(str, n - 1, startFrom + 1);
			
		
		else {
					
			if (isalpha(startFrom) == 0 && isalpha(n) == 0 )
					checkIfPalindrome = find_error_inPalindrome(str, n - 1, startFrom + 1);
			else{
				if (isalpha(startFrom) == 0)
						find_error_inPalindrome(str, n, startFrom + 1);	
				if (isalpha(n) == 0)
				 	find_error_inPalindrome(str, n - 1, startFrom);
			
			}}}
			else
				checkIfPalindrome = 0;
			
		
		
	

	return (checkIfPalindrome);

}




	


















