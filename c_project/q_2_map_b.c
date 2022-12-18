#include <stdio.h>
#include <string.h>
char squeeze(char* s1, char* s2);

char main()
{
	
	char str_1 [] = "quikc";
	char str_2 [] = "qaykv";
	char aq = squeeze(str_1, str_2);
	printf("%s\n",str_1);		    	

}   



char squeeze(char* str_1, char* str_2)
{
	char i;
	char tamp_a [strlen(str_1)];
	int t = 0;
	for ( i = 0; i < strlen(str_1); i++ ){
	
				if ( i >= strlen(str_2) || str_1[i] != str_2[i] )

					tamp_a[t++] = str_1[i];
					
}

	for (int i = 0; i <strlen(str_1);i++)
		str_1[i] = tamp_a[i];
			    			    	
}
















