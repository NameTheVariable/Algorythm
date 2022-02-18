#include <stdio.h>

int sum(int n)
{
    int sum = n;
    while(n>0){
        sum += n%10;
        n/=10;
    }
    return sum;
}
int main(void)
{
    int array[10001], i, self;
    for(i=1;i<10001;i++){
        self = sum(i);
        if(self < 10001)
            array[self] = 1;
    }
    for(i = 1;i < 10001;i++){
        if(array[i] != 1)
            printf("%d\n", i);
    }
    return 0;
}
