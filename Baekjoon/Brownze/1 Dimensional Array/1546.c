#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
	int n, score, max = 0;
	double sum = 0;
	scanf_s("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf_s("%d", &score);
		sum += score;
		if (max < score)
			max = score;
	}
	printf("%.2lf", (sum / max * 100) / n);
	return 0;
}
