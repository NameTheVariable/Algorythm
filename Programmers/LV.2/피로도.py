def dfs(k, cnt, dungeons, temp):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if not temp[i] and k >= dungeons[i][0]:
            temp[i] = True


def solution(k, dungeons):
    answer = -1
    temp = []
    for i in range(len(dungeons)):
        ...
    return answer
