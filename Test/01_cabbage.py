import sys
sys.setrecursionlimit(10000)
T = int(input())
def in_range(x, y):
    return 0 <= x < m and 0 <= y < n


def dfs(x, y):
    if not in_range(x, y) or visited[x][y] == 1 or graph[x][y] == 0:
        return False

    visited[x][y] = 1
    if graph[x][y] == 1:
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    return True

for i in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    result = 0

    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                result += 1

    print(result)
