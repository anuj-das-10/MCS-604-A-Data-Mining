#include<stdio.h>
int main() {
    int x,y,z, a[10][10][10],i,j,k,b,c;
    printf("\nEntre the dimensions x,y,z");
    scanf("%d%d%d",&x,&y,&z);
    printf("\nEnter the data\n");
    for(i=0;i<x;i++) {
        for(j=0;j<y;j++) {
            for(k=0;k<z;k++) {
                scanf("%d",&a[i][j][k]);
            }
        }
    }

    printf("\nThe entered cube is\n");
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

    printf("Data in first plane\n");
    int sum=0;
    for(i=0;i<1;i++) {
        printf("\n");
        for(j=0;j<y;j++) {
            printf("\n");
            for(k=0;k<z;k++) {
                printf("\t");
                printf("%d",a[i][j][k]);
                sum=sum+a[i][j][k];
            }
        }
    }

    printf("\nThe sum in first plane is=%d\n",sum);
    return 0;
}
