#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//add git control of host file, store log of git inits in seperate file
//add edit option by serial number edit [index] || [-l "link"] [-t "text"] ...
//add remove option by serial number edit -rm [index]...
//add data to footer option 
char* lowcase(char *str);
void syntax_error(char**argv);
int Read_and_Write(char*file,int entry,char**argv,long int arbitrary);	
void markdown_convert(char **argv,int arbitrary);
void starttag(FILE *current,char *tag);
void endtag(FILE *current,char *tag,char *buffer);//pass buffer of appropriate size
void add_https(char*string);
//prototyes
int main(int argc,char*argv[])
{
	char file[100];
	char buffer[300];
	if(argc==1)
		printf("Try %s [-h] or %s [--help]\n",argv[0],argv[0]);
	else if(argc==2)
	{
		if(*argv[1]=='1')
		{
			strcpy(file,"/home/arka/Documents/1VACATION/Learn/links/Links.html");
			sprintf(buffer,"firefox %s",file);
			system(buffer);
		}
		else if(*argv[1]=='2')
		{
			strcpy(file,"/home/arka/Documents/1VACATION/Learn/links/NGOs.html");
			sprintf(buffer,"firefox %s",file);
			system(buffer);
		}
		else if(!strcmp(argv[1],"-h")||!strcmp(argv[1],"--help")||!strcmp(argv[1],"help"))//help
	 		{
	 			printf("\n*This is a small program that manipulates a specific html file\n\
*Kindly note that this command is the first protoype with limited functionality:\n[Add code by ~~~code~~~] into the hyperlink text\n\n\
*Also [filenumber] is:\n\t1 for \"Links.html\",\n\t2 for \"NGOs.html\"\n\
**append new url:\t%s [filenumber] -u \"[url]\" -m \"[hyperlink text]\"\n\
**view the html files:\t%s [filenumber]\n\n",argv[0],argv[0]);	 			
	 		}
	 	else
	 		syntax_error(argv);
	}
	else if(!strcmp(argv[2],"-u")&&!strcmp(argv[4],"-m")&&argc==6)
	{
		if(*argv[1]=='1')add_https(argv[3]);//fix bug later
		printf("Converting text to code(s)");
		markdown_convert(argv,150);
		printf(":\t\tdone\n");
		//find_no()
		Read_and_Write(file,27/*find_no goes here*/,argv,700);//passing the shallow copy for magic
		printf("\nDo you want to open webpage?\t1-yes, 0-no:\n");
		int i=0;scanf("%d",&i);
		if(i)
			system(buffer);
		else 
			printf("Saved changes successfully!\n");
	}
	else
 		syntax_error(argv);
 		

	return 0;
}
void add_https(char*string)
{
	if(string[0]=='h'&&string[1]=='t'&&string[2]=='t'&&string[3]=='p'&&string[4]=='s'&&string[5]==':'&&string[6]=='/'&&string[7]=='/')
	{
		sprintf(string,"https://%s",string);printf("I'm argv[1] inside add_https : %s\n",string);
	}
else if(string[0]=='h'&&string[1]=='t'&&string[2]=='t'&&string[3]=='p'&&string[5]==':'&&string[6]=='/'&&string[7]=='/');
}

char* lowcase(char *str)
{	
	int i=0;
	while(*(str+i)!='\0')
	{
		if((*(str+i)<91)&&(*(str+i)>64))
			*(str+i)+=32;
		i++;
	}
	return str;
}
void endtag(FILE *current,char *tag,char *buffer)//pass the buffer 
{
	int i=0,j=0,flag=0,store;
	char _tag[20];
	sprintf(_tag,"</%s>",tag);
	while(1)
	{	
		fscanf(current,"%c",buffer+i);
		if(*(buffer+i)=='<')
		{	
			store=i;
			flag=1;
			while(*(_tag+j)!='\0')
			{
				if(*(_tag+j)==*(buffer+i))
				{
					j++;i++;
				}
				else
					{flag=0;break;}
			}
			if(flag)
			{
				*(buffer+store)='\0';
				return;
			}
		}
		i++;
	}

}

void starttag(FILE *current,char *tag)//validate
{
	char temp,_tag[20];
	int flag_ = 0,i=0;
	sprintf(_tag,"<%s",tag);
	while(1)
	{
		fscanf(current,"%c",&temp);
		if(temp=='<')
		{	
			flag_ = 1;
			while(*(_tag+i)!='\0')//calculating if <tag is same... and proceeded by '>' or ' '
			{
				if(*(_tag+i)==temp);
				else {flag_ = 0;break;}
				i++;
				fscanf(current,"%c",&temp);
			}
			if(temp=='>')
				return;
			else if(temp==' ')
				continue;
		}
		if (temp=='>'&&flag_==1)
			return;
		else
			continue;
	}
}
void syntax_error(char**argv)
	{
		printf("\n*Wrong syntax!\nTry help [-h] or [--help] \n\n");
		exit(1);
	}


int Read_and_Write(char*file,int entry,char**argv,long int arbitrary)
{
	char temp[300];
	FILE*p = fopen(file,"r");
	printf("Entering Read_and_store_excess");
	if(!p)
		printf("Error opening file: \"%s\"\n",file);

	int flag=0;
	do
	{
		fscanf(p,"%s",temp);
			if(!strcmp(temp,"</table>"))
			{
				flag = 1;
				break;
			}
	}while(!feof(p));

	if(flag==0)
	{
		printf("\n\nAdd failed: [reached EOF without finding </table>]\n");
		exit(2);
	}
	int i=0;
	char* buffer = (char*)malloc(sizeof(char)*arbitrary);
	char element;
	while(!feof(p))
	{
		fscanf(p,"%c",&element);//after lots of hit and tries
		sprintf(buffer,"%s%c",buffer,element);
	}
	//works perfectly till here	
	fclose(p);
	//reading over
	printf(":\t\tdone\n");
	printf("Writing info and appending excess");
	//starting writing
	p = fopen(file,"r+");
	while(1)
	{		
		fscanf(p,"%s",temp);
			if(!strcmp(temp,"</table>"))
			{
				fseek(p,-8,SEEK_CUR);
				fprintf(p,"\n<tr>\n\t<td>%d.</td>\n\t<td>\n\t\t<a href=\"%s\">\n\t\t%s\n\t\t</a>\
\n\t</td>\n</tr>\n</table>\n",entry,argv[1],argv[3]);
				break;
			}
			
	}
	printf(":\tdone\n");
	printf("printing buffer");
	fprintf(p,"%s",buffer);
	fclose(p);
	printf(":\t\t\tdone\n");
	return 0;
}
void markdown_convert(char **argv,int arbitrary)
{
	int i=0;
	int count=0;
	char* buffer1 = (char*)malloc(sizeof(char)*arbitrary);
	char* buffer2 = (char*)malloc(sizeof(char)*arbitrary);
	while(*(argv[5]+i)!='\0')
	{
		
		if(*(argv[5]+i)=='~'&&*(argv[5]+i+1)=='~'&&*(argv[5]+i+2)=='~')
		{
			count++;
			sprintf(buffer2,"%s",argv[5]+i+3);//after ```
			if(i==0)
				sprintf(buffer1,"\0");
			
			if(count%2!=0)
			{
				sprintf(argv[5],"%s<code>%s",buffer1,buffer2);
				sprintf(buffer1,"%s<",buffer1);
			}
			else
			{
				sprintf(argv[5],"%s</code>%s",buffer1,buffer2);
				sprintf(buffer1,"%s<",buffer1);
			}
		}
		else
		{
			*(buffer1+i)=*(argv[5]+i);
			*(buffer1+i+1)='\0';
		}
		i++;
	}
	free(buffer1);
	free(buffer2);
}
