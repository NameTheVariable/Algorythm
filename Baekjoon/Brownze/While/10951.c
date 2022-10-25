#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(void) {
	int a, b;
	while (scanf_s("%d %d", &a, &b) != EOF){
		printf("%d\n", a + b);
	}
	return 0;
}
