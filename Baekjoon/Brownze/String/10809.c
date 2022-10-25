#include <stdio.h>
int main(void)
{
    char string[100] = { 0 };
    scanf("%s", string);
    for (int i = 97; i <= 122; i++) {
        int j = 0;
        while (string[j] != 0) {
            if (string[j] == (char)i) break;
            j++;
        }
    if (string[j] == (char)i) printf("%d ", j);
    else printf("-1 ");
    }
}
