#include<stdio.h>
int main()
{
int choice1,b,c,d,e,f,g;
//*******************************
int a[3][3][3]={{40,20,10,20,30,10,30,40,20},{10,10,20,20,10,20,25,21,10},{30,25,10,20,30,15,20,30,25}},i,j,k,x=3,y=3,z=3;
/*printf("\nEntre the dimensions x,y,z");
scanf("%d%d%d",&x,&y,&z);
printf("\nEnter the data\n");
for(i=0;i<x;i++)
{
for(j=0;j<y;j++)
{
for(k=0;k<z;k++)
{
scanf("%d",&a[i][j][k]);
}
}
}
*/
	printf("\nThe Datacube Choosen is>>>>>\n");
	for(i=0;i<x;i++) {
		printf("\n");
			for(j=0;j<y;j++) {
				printf("\n");
				for(k=0;k<z;k++) {
					printf("\t");
					printf("%d",a[i][j][k]);
				}
			}
		}
	//***********************************
		printf("\nWhat operation you want to perform (1. Slicing\t 2. Dicing): Choose any one please>>>\t");
		scanf("%d",&choice1);
	switch(choice1) {
	case 1: {
		printf("\nOK!!!!!!!!!!!  You have Choosen for Slicing! Happy Mining!!!!!\n");
		//******************	
		int dir, s1,s2,s3;
		printf("\nEnter Your Slicing Option (1 for X Axis, 2 for Y Axis and 3 for Z Axis)>>> ");
		scanf("%d",&dir);
		printf("\nYou have choosen %d Axis\n",dir);
		//Program for Slicing operation in X-Axis**************************************************************
		switch(dir)
		{
		case 1:
		{
		
		int temp1, temp;
		printf("Choose Any one Slice out of the %d-Axis \n",dir);
		printf("(");
		for(temp1=0;temp1<x;temp1++)
		{
		printf("\t%d\t",temp1+1);
		}
		printf(")>>>");
		scanf("%d",&temp);
		temp=temp-1;
		printf("Your intended slice is:\n");
		for(s1=temp;s1<=temp;s1++)
		{printf("\n");
		for(s2=0;s2<y;s2++)
		{
		printf("\n");
		for(s3=0;s3<z;s3++)
		{printf("\t");
		printf("%d",a[s1][s2][s3]);
		}
		}
		}
		break;
		}
		//break;
		//Program for Slicing operation in X-Axis********************************************************
		case 2:
		{
		int temp1, temp;
		printf("Choose Any one Slice out of the %d direction following:\n",dir);
		printf("(");
		for(temp1=0;temp1<y;temp1++)
		{
		printf("\t%d\t",temp1+1);
		}
		printf(")>>>");
		scanf("%d",&temp);
		temp=temp-1;
		printf("\nYour intended slice is:\n");
		for(s1=0;s1<x;s1++)
		{printf("\n");
		for(s2=temp;s2<=temp;s2++)
		{
		printf("\n");
		for(s3=0;s3<z;s3++)
		{printf("\t");
		printf("%d",a[s1][s2][s3]);
		}
		}
		}
		break;
		}	
		//Program for Slicing operation in X-Axis********************************************************
		case 3:
		{
		int temp1, temp;
		printf("Choose Any one Slice out of the %d direction:  ",dir);
		printf("(");
		for(temp1=0;temp1<z;temp1++)
		{
		printf("\t%d\t",temp1+1);
		}
		printf(")>>>");
		scanf("%d",&temp);
		temp=temp-1;
		printf("\nYour intended slice is:\n");
		for(s1=0;s1<x;s1++)
		{printf("\n");
		for(s2=0;s2<y;s2++)
		{
		printf("\n");
		for(s3=temp;s3<=temp;s3++)
		{printf("\t");
		printf("%d",a[s1][s2][s3]);
		}
		}
		}
		break;
		}
		//break;********************************************************/
		default:
		{
		break;
		}
				
		}
	//**********************	
	break;
	}
	case 2:
		{
		printf("\nIn the next Class Buddy !!!!!Wait a bit!!!!!!!!!!!!!!!!!!\n");
		
		
	break;
	}
	default:
	{
	printf("\nEoExecution");
	break;
	}
	}
	printf("\n");
	return 0;
}
