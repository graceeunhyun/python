start = list(input())
#print(start)

# 그 행렬을 이제 돌아서 오는 숫자를 구한다.
count = 0
steps = [(-2, -1), (2, -1), (2, 1), (2, -1), (-2, -1), (-1, -2), (-1, 2), (1, 2), (1,-2), (-1, -2)]
col = int(start[1])-1
row = int(ord(start[0]))-97

#print(col, row)

for step in steps:
    newCol = step[0]+col
    newRow = step[1]+row

    if 0<=newCol<8 and 0<=newRow<8:
        count+=1

print(count)