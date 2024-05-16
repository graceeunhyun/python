import sys
from collections import deque
sys.setrecursionlimit(1000000)

n = int(input())
arr = []
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

maxCount = 0
# 욕심쟁이 판다 문제
# 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 전 지역보다 대나무가 많이 있어야 한다.
# 해당 문제를 bfs 로 풀려다가 메모리 초가과 나서 안되고 이를 이제 dp 문제로 풀어야한다.
dxs, dys = [1, -1, 0,0], [0,0, 1,-1]
dp = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] =1

    for dx, dy in zip (dxs, dys):
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] > arr[x][y]:
            # 여기서 dp 재귀로 이용하여 탐색
            dp[x][y] = max(dfs(nx, ny)+1, dp[x][y]) # 네 면을 다 돌았을 때 가장 가능한 것의 maximum 을 구한다. 그걸 dp[x][y] 로 

    return dp[x][y]


answer =1
for i in range(n):
    for j in range(n):
        answer = max(dfs(i, j), answer)


print(answer)

