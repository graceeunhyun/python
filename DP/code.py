pw = input()
answer = 0
match = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

def findPassword(pw):
    n = len(pw)
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1 if pw[0] != '0' else 0

    # 동적 계획 법으로 풀 수 있다.
    for i in range(2, n+1):
        # 한 자리로 보는 경우
        if pw[i-1] != '0':
            dp[i] +=dp[i-1]

        # 두 자리로 보는 경우
        if pw[i-2:i] >= '10' and pw[i-2:i] <= '26':
            dp[i] +=dp[i-2]

    return dp[n]

answer = findPassword(pw)
print(answer%1000000)