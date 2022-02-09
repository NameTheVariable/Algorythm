#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(void) {
	int n = 0;
	int num[9] = {0};
	int index = 0;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &num[i]);
		if (n < num[i]) {
			n = num[i];
			index = i;
		}
	}
	printf("%d\n%d", n, index + 1);
}
//num[9]는 9개의 element를 가진 array이며 이 array안의 element들은 0으로 초기화 해준다
//scanf에서 num[i]의 element들을 받는다.
//이때 element(index)는 0부터 시작이므로 마지막 출력에서 index는 0부터 시작이므로 1을 더해준다.
