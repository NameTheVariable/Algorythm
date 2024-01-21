def solution(n):
    answer = 0
    fibo = 0
    if(n == 1):
        fibo = 0
    else:
        for i in range(n):
            fibo = i-1 + i
    # answer = fibo % 1234567
    return fibo

print(solution(3))