/* Postfix and Prefix Expression in Same Statement*/

#include<stdio.h>
#include<conio.h>
void main() {
int i = 0, j = 0;
j = i++ + ++i;
printf("%d\n %d\n", i,j);

}