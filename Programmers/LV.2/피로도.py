answer = 0


def backtracker(k, cnt, dungeons, temp):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if not temp[i] and k >= dungeons[i][0]:
            temp[i] = True
            backtracker(k - dungeons[i][1], cnt + 1, dungeons, temp)
            temp[i] = False


def solution(k, dungeons):
    global answer
    temp = [False] * len(dungeons)
    backtracker(k, 0, dungeons, temp)
    return answer
