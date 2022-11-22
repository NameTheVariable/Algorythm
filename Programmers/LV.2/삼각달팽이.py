def solution(n):
    snail = [[0] * n for _ in range(n)]
    answer = []
    row, col = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            elif i % 3 == 2:
                row -= 1
                col -= 1
            snail[row][col] = num
            num += 1
    for i in range(n):
        for j in range(i+1):
            answer.append(snail[i][j])

    return answer
