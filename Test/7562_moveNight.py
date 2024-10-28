from collections import deque

# 테스트 케이스의 input 을 받는다
t = int(input())
# 해당 테스트 케이스만큼 이제 결과를 출력해야한다.
for i in range(t):

    #첫째줄 : 체스판의 한변의 길이
    length = int(input())
    arr = [[0 for _ in range(length)] for _ in range(length)]

    #둘째줄 : 현재 칸
    curX, curY = map(int, input().split())
    #셋째줄 : 이동하고 있는 칸
    aimX, aimY = map(int, input().split())

    #나이트가 최소 몇 번 만에 이동할 수 있는지 출력한다
    count = 0
    dxs, dys = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]
    # while 문 끝나는 시점: curx, curY 이 aimX, aimY 에 갈 때 끝난다.

    #해당 로직을 BFS 를 이용해서 구할 수 있다. 처음의 로직은 최단거리를 구할 수 없었음.
    queue = deque([(curX, curY, count)])

    #방문한 위치를 기록한다
    visited = [[False for _ in range(length)] for _ in range(length)]
    visited[curX][curY] = True

    while queue:
        x, y, count = queue.popleft()
        #print(x,y, count, "처음")

        #빠져나올 조건
        if x == aimX and y == aimY:
            print(count)
            break

        for dx, dy in zip(dxs, dys):
            nextX = x+dx
            nextY = y+dy

            if (0<=nextX<length and 0<=nextY<length) and not visited[nextX][nextY] :
                queue.append((nextX, nextY, count+1))

                #방문한거 표시
                visited[nextX][nextY] = True



