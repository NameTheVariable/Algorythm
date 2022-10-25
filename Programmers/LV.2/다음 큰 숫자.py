def count_bin_one(i):  # binary로 변환한 숫자의 1의 갯수를 세는 함수
    binarynumber = bin(i)
    count_one = binarynumber.count('1')
    return count_one


def solution(n):
    answer = n
    num = count_bin_one(n)
    while True:
        answer += 1
        if int(count_bin_one(answer)) == num:
            return answer
