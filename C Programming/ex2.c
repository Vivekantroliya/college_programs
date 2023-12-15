//factorial(n) computation using recursion



void main(){
    long factorial(long);
    long fact;
    long n;
    printf("\nEnter a Number:");
    scanf("%d",&n);

    fact = (long)factorial(n);
    printf("\nThe Factorial of ");
    printf("%d! is %d.",n,fact);
}

//Recurive Factorial Computation

    long factorial(long n){
        long fact=1;
        if(n<1){
            return 1;
        }
        else{
            return((long)n*factorial(n-1));

        }
    }
