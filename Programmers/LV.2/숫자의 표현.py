def solution(n):
    a = 0
    for i in range(1, n):
        b = i
        for j in range(i + 1, n):
            b += j
            if b == n:
                a += 1
                break
            elif b > n:
                break
    answer = a + 1
    return answer
