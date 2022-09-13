def solution(s):
    answer = ''

    numbers = list(map(int, s.split(' ')))

    minimum = min(numbers)
    maximum = max(numbers)
    answer = str(minimum) + ' ' + str(maximum)

    return answer
