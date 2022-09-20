from collections import defaultdict, deque


def solution(n, road, k):
    graph = defaultdict(list)
    for x, y, distance in road:
        graph[x].append((y, distance))
        graph[y].append((x, distance))

    visited = [0 for _ in range(n + 1)]
    queue = deque([(1, 0)])
    visited[1] = 1

    while queue:
        node, distance = queue.popleft()

        for v, w in graph[node]:
            if distance + w <= k and (not visited[v] or distance + w <= visited[v]):
                queue.append((v, distance + w))
                visited[v] = distance + w

    answer = n + 1 - visited.count(0)

    return answer
