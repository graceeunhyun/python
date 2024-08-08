n, s = map(int, input().split())
arr = []
for i in range(n):
    val = map(int, input().split())
    arr.append(val)

# 문제를 해결하기 위해 : DP 다이나믹 프로그래밍 접근 방식을 사용할 수 있음.

def maximize_profit(pictures, S):
    n = len(pictures)
    pictures.sort(key=lambda x: x[0]) # sort by price
    # 그림을 높이 기준으로 정렬

    dp = [0] * n
    total_max_profit = 0

    for i in range(n):
        h_i, p_i = pictures[i]
        if h_i >=s:
            dp[i] = p_i

        for j in range(i):
            h_j, p_j = pictures[j]
            if h_i - h_j >= s:
                dp[i] = max(dp[i], dp[j] + p_i)
