r, c= map(int, input().split())
arr = []
start = []
for i in range(r):
    val = list(input().split())
    if 'J' in val:
        j = val.index('J')
        start = [i,j]
    arr.append(val)

count = 0

# j 가 두 세개 일 수 있으니깐
# queue 에 넣어서 처리해야한다.
def inRange(x,y):
    return 0<=x<r and 0<=y<c

def processFire(i, j):
    global count
    count +=1

    dxs, dys = [1, -1, 0,0], [0,0,1,-1]
    for dx, dy in zip(dxs, dys):
        nx, ny = i+dx, j+dy
        if inRange(nx, ny) and arr[i][j] == '.':
            arr[nx][ny] = 'X'
            count+=1
            processFire(nx, ny)

        if inRange(nx, ny) and arr[i][j] == 'F':
            arr[nx][ny] = 'F'


processFire(start[0], start[1])
print(count)