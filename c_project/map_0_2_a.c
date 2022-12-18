#include <stdio.h>
#include <ctype.h>

int chack_Password_len(char s[ ]);
int chackPossword(char s[ ]);


int main()
{
	char s[] = {'1','3','4','3','9','3','%','S','A'};
	int password_length = chack_Password_len(s);
	if( password_length < 5)
	{
			printf("the password is lower try agen");
			return 0;
	}
	int condition = chackPossword(s);
}
	
	


int chack_Password_len(char s[ ])
{
	int password_length = 0;
	while ( s[password_length] != '\0')
		password_length = password_length + 1;
		
	return password_length;
}

int chackPossword(char s[ ])
{
	int cuonter_1 = 1;
	int cuonter_2 = 1;
	int cuonter_3 = 1;
	 
		
		
		for (int i = 1; s[i]!= '\0' ; i++)
		{
			if (isdigit(s[i]) == 0)
				 cuonter_1++;
			if (isalpha(s[i]) == 1)
				 cuonter_2++;
			if ( s[i] == ("%" || "!" || "# "|| "@"))
				 cuonter_3++;
			//return 0;	
		}
	
	
	if (cuonter_1 && cuonter_2 && cuonter_3 >= 4)
		printf("the password is sronger");
	else 
		printf("the password is lower try agen");
	return 1;
}

















