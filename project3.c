/*Whenever more than one format specifiers (i.e %d) are directly or indirectly related with
same variable (i,i++,++i) then we need to evaluate each individual expression from right
to left.*/
#include<stdio.h>
void main() {
int i = 1;
printf("%d %d %d", i, ++i, i++);

}