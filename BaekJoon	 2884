#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(void) {
	int h, m, total, newh, newm; 
	scanf("%d %d", &h, &m);
	total = 60 * h + m - 45;
	newh = total/60;
	newm = total%60;
	if (newm >= 0)
		printf("%d %d", newh, newm);
	else if (newm < 0)
		printf("%d %d", 23-newh, 60 + newm);
	return 0;
}
