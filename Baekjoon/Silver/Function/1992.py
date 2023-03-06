import sys
input = sys.stdin.readline

n = int(input())
vid = [input().strip() for _ in range(n)]
answer = ""


def quad(x, y, n):
    check = vid[x][y]
    global answer
    for row in range(x, x + n):
        for col in range(y, y + n):
            if check != vid[row][col]:
                answer += '('
                quad(x, y, n // 2) # 1
                quad(x, y + n // 2 , n // 2) # 2
                quad(x + n // 2, y , n // 2) # 3
                quad(x + n // 2, y + n // 2, n // 2) # 4
                answer += ')'
                return
    if check == '0':
        answer += '0'
    else:
        answer += '1'
    return None


quad(0, 0, n)
print(answer)
