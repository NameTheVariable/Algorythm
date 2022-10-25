#include <stdio.h>

long long sum(int *a, int n) {
	long long ans = 0;
    for(int i = 0; i < n; i++){
        ans += a[i];
    }
	return ans;
}
//ans에 array a[i]만 계속해서 더해주는 부분만 구현하면 되는 문제였다.
