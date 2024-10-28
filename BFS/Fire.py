from collections import deque

r, c = map(int, input().split())
arr = []
for i in range(r):
    val = list(input())
    arr.append(val)

# J에서 출발하는 지훈이가 1개 이상의 지점에서 출발할 수 있으니 이를 구한다.
jList = deque()
# 불의 경우 각 지점에서 네 방향으로 확산되므로 이에 대한 부분을 구한다.
fireList = deque()

# 로직
# 지훈이가 불에 타기 전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정
# BFS로 구해보자.
visitedF=[[-1 for _ in range(c)] for _ in range(r)]
visitedJ=[[-1 for _ in range(c)] for _ in range(r)]


for i in range(r):
    for j in range(c):
        if arr[i][j] == 'F':
            fireList.append((i, j))
            visitedF[i][j] = 0
        elif arr[i][j] == 'J':
            jList.append((i, j))
            visitedJ[i][j] = 0
def final_grid(x, y):
    return (x <0 or x > r - 1 or y < 0 or y > c - 1)

def is_range(x, y):
    return 0 <= x < r and 0 <= y < c

def bfs():
    count = 0
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    while fireList:
        # 불 확산
        x, y = fireList.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and visitedF[nx][ny] == -1 and arr[nx][ny] !='#':
                visitedF[nx][ny] = visitedF[x][y]+1
                fireList.append((nx, ny))


    while jList:
        # J에 대해서 왔다갔다
        x, y = jList.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_range(nx, ny):
                if visitedJ[nx][ny] == -1 and arr[nx][ny] != '#' and (visitedF[nx][ny] == -1 or visitedF[nx][ny] > visitedJ[x][y]+1):
                    # 불보다 지훈이가 빨리 도착한 경우
                        visitedJ[nx][ny] = visitedJ[x][y] +1
                        jList.append((nx, ny))
                        #print(jList)

            else:
                return visitedJ[x][y]+1

    return "IMPOSSIBLE"


print(bfs())


