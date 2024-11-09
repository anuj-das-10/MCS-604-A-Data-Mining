#include<stdio.h>
#include<stdlib.h>

#define X 7
#define Y 4
#define Z 2 


void print3D(int data[Z][Y][X], int x, int y, int z) {
    int i, j, k;
    printf("{");
    for(i = 0; i < x; i++) {
        printf("{\n");
        for(j = 0; j < y; j++) {
            printf("{");
            for(k = 0; k < z; k++) {
                printf("%d ", data[i][j][k]);
            }
            printf("}\n");
        }
        printf("}\n");
    }
    printf("}\n");
}

void main() {
    int data[Z][Y][X] = {
        {{2017, 150, 170, 130, 160, 110, 125}, 
        {2018, 140, 160, 120, 130, 100, 110}, 
        {2019, 130, 145, 125, 145, 95, 120}, 
        {2020, 145, 130, 135, 140, 105, 115}},

        {{2017, 145, 155, 120, 150, 90, 120}, 
        {2018, 138, 146, 115, 140, 85, 105}, 
        {2019, 132, 142, 130, 140, 75, 120}, 
        {2020, 140, 148, 125, 145, 80, 90}}
    };

    print3D(data, Z, Y, X);

}