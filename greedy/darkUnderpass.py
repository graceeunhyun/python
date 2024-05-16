# 굴다리의 개수
n = int(input())
# 가로등의 개수
m = int(input())

# m 개의 설치할 수 있는 가로등의 위
list = map(int, input().split())
boolean = False

# binary search 로 해당 부분을 구현해보고자 한다.
start = 1
end = max(list)

result = 0
while start<=end:
    mid = start + end//2
    total = 0

    for x in arr:

