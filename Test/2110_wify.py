n, c = map(int, input().split())
arr = []
# 공유기의 좌표를 입력 받는다
for i in range(n):
    arr.append(int(input()))

# 가장 인접한 두 공유기 사이의 최대 거리를 출력
dist = 0

# 공유기의 좌표를 정렬, 이진탐색을 위해서 정렬한다
arr.sort()

#가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치 할 수 있는 최대 거리를 찾는다
start = 1
end = arr[n-1] - arr[0]

while start <=end:
    mid = (start + end) // 2
    value = arr[0]
    count = 1

    # 각 공유기 사이의 거리가 mid 보다 크거나 같으면 공유기를 설치한다
    for i in range(1, n):
        if arr[i] >= value + mid:
            value = arr[i]
            count += 1

    # 공유기의 개수가 c 보다 크거나 같으면 mid 값을 늘려본다
    if count >= c:
        start = mid + 1
        dist = mid
    # 공유기의 개수가 c 보다 작으면 mid 값을 줄여본다
    else:
        end = mid - 1

print(dist)