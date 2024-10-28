n, m = map(int, input().split())
arr = []
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

print(arr)

result = 0
for i in range(n):
    val = min(arr[i])
    result = max(val, result)
print(result)