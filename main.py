n = int(input())
arr = []
for i in range(n):
    val = int(input())
    arr.append(val)

total = arr[0]
visited = [0]*n

step = 0
count = 0

#연속된 세 계단을 더해선 안된다
while(step+2 < n-1):

    if count == 2:
        step += 1
        count = 0
        continue

    if arr[step+2] > arr[step+1]:
        total += arr[step+2]
        step += 2
    else:
        total += arr[step+1]
        step += 1

    count +=1
    print(step, total)


total +=arr[n-1]
print(total)