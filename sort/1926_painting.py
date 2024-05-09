import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
arr = []
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

count = 0
width = 0
curWidth = 0
# 그림의 개수를 구하는 문제로 dfs 를 통해 1 일 경우 해당 경계를 그림으로 구하는 것이다.

visited=[[0]*m for _ in range(n)]
def in_range(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y):
    global curWidth;
    if not in_range(x,y) or arr[x][y] == 0 or visited[x][y] == 1:
        return False
    visited[x][y] = 1
    curWidth +=1
    if arr[x][y] == 1:
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            if dfs(i,j):
                count += 1
                width = max(width, curWidth)
                curWidth = 0

print(count)
print(width)