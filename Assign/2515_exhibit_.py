import bisect
import sys
# n 은 그림의 갯수
# s 는 판매가능 그림의 높이를 나타내는 정수

n, s = map(int, input().split())
arr = []
# 한 그림의 높이와 가격을 나타내는 정수
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

dp =[0]*n
# result: 핀메가능 액자들의 가격의 합이 최대가 되도록 배치
arr.sort()
#print(arr)
result = 0

for i in range(n):
    h_i, p_i = arr[i]
    #기본적으로 p_i 가 최대값이라고 가정한다.
    dp[i] = p_i
    maxprofit = 0
    for j in range(n):
        h_j, p_j = arr[j]
        #보이는 부분에 해야되니깐 아래와 같은 코드가 나온 것이다.
        if h_j >= h_i:
            continue

        visible = h_i - h_j
        if visible >= s:
            # dp[i] = max(dp[i], dp[j]+p_i)
            # 이렇게 하면 시간복잡도가 줄어서
            maxprofit = max(maxprofit, dp[j])
    dp[i] = max(dp[i], maxprofit+arr[i][1])


result = max(dp)
print(result)