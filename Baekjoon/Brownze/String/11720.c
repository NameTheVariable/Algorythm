int main(void)
{
    int n, sum = 0;
    scanf("%d", &n);
    char array[n];
    scanf("%s", array);
    for(int i = 0; i < n; i++)
        sum += array[i] - '0';
    printf("%d", sum);
    return 0;
}
