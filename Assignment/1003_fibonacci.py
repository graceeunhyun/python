# python 시간 복잡도 줄이기
# 1. memoization 으로 줄여보자
t = int(input())

memo ={}
def fibonacci(n):
    global memo0, memo1
    # if n != 0 and n != 1 and n in memo:
    #     return memo[n]

    if n == 0:
        memo0 += 1
        return 0
    elif n == 1:
        memo1 += 1
        return 1

    else :
        result = fibonacci(n-1) + fibonacci(n-2)
        # memo[n] = result
        return result


for i in range(t):
    # n 번째 피보나치를 구하고 0 출력되는 수랑 1번째 출력되는 수를 구하자
    n = int(input())
    memo0, memo1 = 0, 0 # Reset counts for each test case

    fibonacci(n)
    print(memo0, memo1)

