/* Conditional Operator*/
#include <stdio.h>
int main(){
char February;
int days;
printf("If this year is leap year, enter 1. If not enter any integer: ");
scanf("%c",&February);
// If test condition (February == 'l') is true, days equal to 29.
// If test condition (February =='l') is false, days equal to 28.

/*Syntax : condition ? exp1 : exp2;
It first evaluate the condition, if it is true (non-zero) then the “exp1” is
evaluated, if the condition is false (zero) then the “exp2” is evaluated.*/
days = (February == '1') ? 29 : 28;
printf("Number of days in February = %d",days);
return 0;
}