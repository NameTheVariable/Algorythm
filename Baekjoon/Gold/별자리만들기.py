# 별자리 만들기
import heapq
import sys
import math

readLine = sys.stdin.readline
result = 0
starNum = int(readLine())  # 별들의 개수
starArr = []  # 별들을 집어넣을 리스트

# 별들의 좌표값을 map 안에 저장해준다.
for i in range(starNum):
    x, y = map(float, readLine().split())
    starArr.append((x, y))

vertex = [[] for _ in range(starNum)]

for i in range(starNum):
    j = i + 1
    for j in range(starNum):
        xPos, yPos = starArr[i][0], starArr[i][1]
        nextXpos, nextYpos = starArr[j][0], starArr[j][1]
        # 별들 사이의 거리 구하기
        distance = math.sqrt(abs(xPos - nextXpos) ** 2 + abs(yPos - nextYpos) ** 2)
        vertex[i].append((distance, j))
# 방문했는지를 체크하는 리스트
visited = [False] * starNum


def prim(s):
    global result
    q = []
    heapq.heappush(q, (0, s))
    while q:
        distance, node = heapq.heappop(q)
        if not visited[node]:
            result += distance
            visited[node] = True
        for nextDistance, nextNode in vertex[node]:
            if not visited[nextNode]:
                heapq.heappush(q, (nextDistance, nextNode))


prim(0)
print(f'{result:.2f}')
