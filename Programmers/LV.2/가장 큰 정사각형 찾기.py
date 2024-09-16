def solution(board):
    # 행과 열의 길이
    rows, cols = len(board), len(board[0])
 
    # 2차원 DP 배열 초기화
    dp = [[0] * cols for _ in range(rows)]

    # 첫 번째 행과 첫 번째 열은 그대로 복사
    for i in range(rows):
        dp[i][0] = board[i][0]

    for j in range(cols):
        dp[0][j] = board[0][j] 

    # 동적 프로그래밍을 통한 정사각형 크기 갱신
    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                print(dp)

    # 최대 정사각형의 한 변 길이 구하기
    max_side = max(map(max, dp))
    print(max_side)

    # 넓이 반환
    return max_side * max_side

board = [
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1]
]

# 결과 출력
solution(board)