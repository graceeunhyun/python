import sys
sys.setrecursionlimit(10000)
n = int(input())

#적록 색약의 경우 빨강 초록을 이제 구분하지 못한다.
#따라서 빨강을 초록으로 바꾸어도 같은 색으로 인식한다.
arr=[]
for i in range(n):
    val = input()
    arr.append(val)

visited = [[0 for _ in range(n)] for _ in range(n)]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def dfs(x,y, color):
    if not in_range(x,y) or visited[x][y] == 1 or arr[x][y] != color:
        return False

    visited[x][y] = 1

    if arr[x][y] == color:
        dfs(x+1, y, color)
        dfs(x-1, y, color)
        dfs(x, y+1, color)
        dfs(x, y-1, color)
        return True


result = 0
noRed = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j, arr[i][j]):
            result +=1

#적록 색약의 경우 다 빨간색을 그린으로 바꾸자
arr_rg = [['G' if c =='R' else c for c in row] for row in arr]
arr = arr_rg

visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs(i, j, arr[i][j]):
            noRed +=1

print(result, noRed)