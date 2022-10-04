def is_possible(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i] - col[x]) == x - i:
            return False
    return True


def dfs(x):
    global resource
    if x == n:
        resource += 1
        return
    for i in range(n):
        col[x] = i
        if is_possible(x):
            dfs(x + 1)


n = int(input())
resource = 0
col = [0] * n
dfs(0)
print(resource)
