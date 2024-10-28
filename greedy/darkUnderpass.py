
# 굴다리의 개수
n = int(input())
# 가로등의 개수
m = int(input())

# m 개의 설치할 수 있는 가로등의 위
array = list(map(int, input().split()))
boolean = False

# binary search 로 해당 부분을 구현해보고자 한다.
start = 0
end = n
result = 0

def illustrate(height, positions):
    check = [False] * (n+1)

    for pos in positions:
        left = max(0, pos - height)
        right = min(n, pos+height)
        for i in range(left, right+1):
            check[i] = True


    #print(all(check), check, height)

    #이렇게 해주는 이유는 굴다리는 n+1 부터 시작되기 때문이다
    for i in range(1, n+1):
        if positions[i] == False:
            return False

    return True


while start<=end:
    mid = (start + end)//2
    total = 0

    # 현재 높이로 굴다리를 밝히는지 확인
    if illustrate(mid, array):
        end = mid -1
        result = mid
    else:
        start = mid+1
print(result)

