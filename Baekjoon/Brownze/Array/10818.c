#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(void) {
	int n, num;
	int min = 1000001, max = -1000001;

	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &num);
		if (num > max)
			max = num;
		if (num < min)
			min = num;
	}
	printf("%d %d", min, max);
	return 0;
}
