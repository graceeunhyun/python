n = int(input())
array = set(map(int, input().split()))

# m 손님이 확인요청한 부품 개수 입력
m = int(input())
list = list(map(int, input().split()))

# 손님 꺼 있는지 확인
for i in list:
    #해당 부품이 있는지 array 돌면서 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')