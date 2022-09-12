from itertools import combinations


def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    temp = list(combinations(numbers, 3))
    for array in temp:
        if isprime(sum(array)) is True:
            answer += 1
    return answer
