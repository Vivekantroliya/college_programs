#include<stdio.h>

void main(){
    int a[10],i,s=0;
    for(i=0;i<10;i++){
        printf("enter number %d",i+1);
        scanf("%d", &a[i]);
    }
    printf("enter value to be searched:");
    scanf("%d", &s);
    for(i=0;i<10;i++){
        if(a[i]==s){
            s=a[i];
            printf("value %d found on\n %d position",s,i+1);
            break;
        }

    }


}
