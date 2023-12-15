//factorial(n) computation using iteration

#include<stdio.h>
#include<conio.h>

void main(){
    int factorial(int);
    int fact;
    int n;
    printf("\nEnter a Number:");
    scanf("%d",&n);

    fact = factorial(n);
    printf("\nThe Factorial of ");
    printf("%d! is %d.",n,fact);
}

/*interactive factorial computation*/

    int factorial(int n){
        int fact=1;
        while(n>1){
            fact=fact*n;
            n--;
        }
        return fact;
    }
