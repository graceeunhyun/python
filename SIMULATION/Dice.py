n, m, r, c = map(int, input().split())
direction = list(input().split())
# 주사위 문제로 해당 문자가 돌아간 순서대로 된다.
visited = [[0]*n for _ in range(n)]
dice=[1,2,3,4,5,6]
sum = 0
def roll_dice(dice, dir):
    global r, c
    if dir == 'L':
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
        c-=1
    elif dir =='R':
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
        c+=1
    elif dir =='U':
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
        r-=1
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
        r+=1
r = r-1
c = c-1
visited[r][c] = 6

def is_range(x,y):
    return 0<=x<n and 0<=y<n

for i in range(m):
    roll_dice(dice, direction[i])
    if is_range(r,c):
        visited[r][c] = dice[5]

for i in range(n):
    for j in range(n):
        sum+=visited[i][j]

print(sum)