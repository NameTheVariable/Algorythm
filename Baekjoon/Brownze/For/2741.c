#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(void) {
	int n;
	scanf_s("%d", &n);
	for (int i = 1; i <= n; i++) {
		printf("%d\n", i);
	}
	return 0;
}
