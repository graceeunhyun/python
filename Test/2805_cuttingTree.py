# 나무의 수, 상근이가 집으로 가져가려는 하는 나무의 길이 m
n, m = map(int, input().split())
#나무의 높이
arr = list(map(int, input().split()))

# binary search 로 풀 수 있음
start = 0
end = max(arr)
result  = 0

while start<=end:
    mid = (start+end)//2
    total = 0

    # 돌면서 떡의 길이를 계산한다
    for x in arr:
        if x>mid:
            total+=x-mid

    if total >= m:
        result = max(result, mid)
        start = mid+1
    else:
        end = mid-1

print(result)

