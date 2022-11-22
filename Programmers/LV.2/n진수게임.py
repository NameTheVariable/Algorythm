def trans(number, n):
    element = "0123456789ABCDEF"
    temp = ""
    if number == 0:
        return '0'
    while number > 0:
        number, remain = number // n, number % n
        temp += element[remain]
    return temp[::-1]


def solution(n, t, m, p):
    answer = ''
    game = ''
    for _ in range(t * m):
        game += trans(_, n)
    while len(answer) < t:
        answer += game[p-1]
        p += m
    return answer
