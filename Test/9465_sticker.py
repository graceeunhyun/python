def max_sticker_score(n, sticker):
    if n == 0:
        return 0
    if n == 1:
        return max(sticker[0][0], sticker[1][0])

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if n > 1:
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]

    for j in range(2, n):
        dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + sticker[0][j]
        dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + sticker[1][j]

    return max(dp[0][n - 1], dp[1][n - 1])


# 여러 테스트 케이스를 입력 받음
t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(2):
        val = list(map(int, input().split()))
        arr.append(val)

    # 각 테스트마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최대값을 출력
    print(max_sticker_score(n, arr))
