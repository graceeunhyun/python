n, m = map(int, input().split())
arr = []
for i in range(n):
    val = list(map(int, input()))
    arr.append(val)

print(arr)


def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False

    if arr[x][y] ==0:
        arr[x][y] = 1
        dfs(x+1,y)
        dfs(x, y+1)
        dfs(x-1,y-1)

        return True

result = 0
for i in range(n):
    for j in range(m):
       if dfs(i,j):
           result+=1

print(result)