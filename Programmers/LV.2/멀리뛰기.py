
def solution(n):
    # (n-1칸 뛴 후 1칸 뛰는 가짓수) + (n-2칸 뛴 후 2칸 뛰는 가짓수)
    step = dict()
    step[0], step[1] = 1, 1
    for i in range(2, n+1):
        step[i] = step[i-2] + step[i-1]

    return step[n] % 1234567
