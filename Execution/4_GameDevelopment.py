n, m = map(int, input().split())
# x, y 은 startPosition
x, y, dir = map(int, input().split())
count = 0
# 방향을 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

d=[[0]*n for _ in range(m)]
gameMap = []
for i in range(n):
    val = list(map(int, input().split()))
    gameMap.append(val)

def dfs(x,y, visited):
    if visited[x][y] ==1:
        return

    visited[x][y] = 1


def turn_left():
    global dir
    dir = (dir-1)
    if dir ==-1:
        dir = 3

turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    # 왼쪽 방향에 안간 칸이 있따면 회전 에서 전진
    nx = x+dxs[dir]
    ny = y+dys[dir]

    if gameMap[nx][ny] == 0 and d[nx][ny] ==0:
        x = nx
        y = ny
        d[nx][ny] = 1
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1

    # 없다면, 회전만 수행하고 다시 1단계로 돌아감
    if turn_time == 4:
        nx = x-dxs[dir]
        ny = y-dys[dir]
        if gameMap[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time =0
    # 네 방향 이미 가본칸이거나 바다로 되어 있는 경우에는, 바라보는 방향을 유지한 채로, 한 칸 뒤로 가고 1단계로
    # 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우 움직임을 멈춤


print(count)