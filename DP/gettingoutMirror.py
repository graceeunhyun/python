n = int(input())
x, y = map(int, input().split())
x = x - 1
y = y - 1
arr = []
for _ in range(n):
    val = input()  # split()만 사용하여 리스트 생성
    arr.append(val)

visited = [[0 for _ in range(n)] for _ in range(n)]

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


count = 0
direction = 0


def checkCell(x, y, d):
    curX = x + dxs[d]
    curY = y + dys[d]

    if in_range(curX, curY) and arr[curX][curY] == '#':
        return True
    else:
        return False


while True:
    if not in_range(x, y) or visited[x][y] == 1:
        break

    visited[x][y] = 1

    # 바라보고 있는 방향으로 이동이 가능한 경우
    curX = x+dxs[direction]
    curY = y+dys[direction]
    print(x, y, "초기")
    if in_range(curX, curY):
        if checkCell(x, y, (direction - 1) % 4):
            x = curX
            y = curY
            count += 1
        else:
            print("else")
            x = curX
            y = curY
            count += 1
            direction = (direction - 1) % 4  # 시계방향으로 회전
            x = x + dxs[direction]
            y = y + dys[direction]
            count+=1
    print(x, y, direction, count)
    if not in_range(curX, curY):
        direction = (direction + 1) % 4
        continue


print(count)
