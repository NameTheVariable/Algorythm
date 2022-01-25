#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(void) {
	int a, b;
	while (1) {
		scanf_s("%d %d", &a, &b);
		if (a == 0 && b == 0) break;
		printf("%d\n", a + b);
	}
	return 0;
}
