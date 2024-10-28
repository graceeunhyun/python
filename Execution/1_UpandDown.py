n = int(input())
plan = list(input().split())
print(plan)

# 이동 타입에 대해서 다시 구해보자.
x,y = 1, 1
move = ['L', 'R', 'U', 'D']
dxs = [0,0,-1,1]
dys = [-1,1,0,0]

# simulation 해서 이제 그 좌표치로 가는 것을 구해야한다 .
for p in plan:
    for j in range(len(move)):
        if move[j] == p:
            nextX = x+dxs[j]
            nextY = y+dys[j]
            print(move[j], dxs[j])

    if 1<=nextX<=n and 1<=nextY<=n:
        x = nextX
        y = nextY
        print(x,y)




print(x, y)