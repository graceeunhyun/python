from collections import deque
n, m = map(int, input().split())
arr = []
for i in range(n):
    #구슬 탈출에 관한 데이터를 받을 수 잇음
    val = list(map(int, input().split()))
    arr.append(val)


#파란 구슬을 구멍에 넣지 않으면서 빨간 구슬을 10번 이하로 움직여서 빼낼 수 있으면 1, 없으면 0
#구슬을 손으로 건드릴 수는 없고 중력을 이용해서 굴려야함
# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기

#파란 구슬이 구멍에 빠지면 실패
#빨간 구슬과 파란 구슬이 동시에 빠져도 실패
blueList = deque()
redList = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] =='R' :
            redList.append((i,j))
        elif arr[i][j] =='B' :
            blueList.append((i,j))


 while redList:
     #빨간 구슬의 위치를 찾는다.
        x, y = redList.popleft()
     # #파란 구슬의 위치를 찾는다
     #    bX, bY = blueList.popleft()
     #
