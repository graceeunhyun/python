n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort()

start = arr[0]
end = max(arr)

result = 0
while(start <= end):
    mid = (start + end) // 2
    total = 0

    for x in arr:
        if x > mid:
            total += mid
        else:
            total += x

    if total <= m:
        start = mid + 1
    else:
        end = mid - 1

print(result)
