n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i+1, n):
        if(arr[i] != arr[j]):
            count +=1

print(count)