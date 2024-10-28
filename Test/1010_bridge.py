import math
t = int(input())
def count_bridge_combination(n, m):
    combination = math.factorial(n) / (math.factorial(m) * math.factorial(n - m))
    return combination

for i in range(t):
    n,m = map(int, input().split())

    #강에서 이제 n 개에서 m 을 선택하야하는 조합의 수를 계산해야한다.

    count = (int)(count_bridge_combination(m,n))
    print(count)
