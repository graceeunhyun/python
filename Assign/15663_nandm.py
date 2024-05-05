n, m = map(int , input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []

for i in range(n):
    for j in range(n):
        if i == j:
            continue

