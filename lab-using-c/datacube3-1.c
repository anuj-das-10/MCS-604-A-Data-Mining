#include<stdio.h>
#include<stdlib.h>
int main(){
int choice,i,j,count=0;
   int a[2][4][7]={{{2017,150,170,130,160,110,125},
                   {2018,140,160,120,130,100,110},
                   {2019,130,145,125,146,95,120},
                   {2020,145,130,135,140,105,115}},
                   
                   {{2017,145,155,120,150,90,120},
                   {2018,138,146,115,140,85,105},
                   {2019,132,142,130,140,75,120},
                   {2020,140,148,125,145,80,90}}};
   while(1){
   printf("Enter the slice you want to show:");
   printf("\n 1-Male, \n 2-Female\t, Enter your choice");
   scanf("%d",&choice);
   switch(choice){
   case 1:{
   	printf("\nYou have selected Male:>>>\n");
   	for(i=0;i<4;i++){
   	  printf("%d \t",a[0][i][0]);
   	  for(j=1;j<7;j++){
   	     printf("%d \t",a[0][i][j]);
   	     count+=a[0][i][j];
   	  }
   	  printf("\nCount=%d\n",count);
   	}  
   	break;
   	}
   case 2:{
   	printf("\nYou have selected Male:>>>\n");
   	for(i=0;i<4;i++){
   	  printf("%d \t",a[1][i][0]);
   	  for(j=1;j<7;j++){
   	     printf("%d \t",a[1][i][j]);
   	     count+=a[0][i][j];
   	  }
   	  printf("\nCount=%d\n",count);
   	}  
   
   	break;
   	}
   case 3:{
   	printf("Exiting. \n");
   	exit(0);
   	break;
   	}
   default:
   	exit(0);
   	}
   }
  printf("EoF");
  return 0;
  }
