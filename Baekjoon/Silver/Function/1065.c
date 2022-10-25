#include <stdio.h>

int Hansoo(int n)
{
    if (n < 100)
        printf("%d", n);
    else {
        int i;
        int count;
        int A, B, C;
        count = 99;
        for (i = 100; i <= n; i++) {
            A = i / 100;
            B = (i % 100) / 10;
            C = (i % 100) % 10;
            if ((C - B) == (B - A))
                count++;
        }
        printf("%d", count);
    }
}
int main(void)
{
    int n;
    scanf("%d", &n);
    Hansoo(n);
}
