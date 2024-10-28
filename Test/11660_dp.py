import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
#dp 의 memoization 으로 구해야할거 같음..

for i in range(n):
    val = list(map(int, input().split()))
    graph.append(val)

arr = []
memo = [[0]*n for _ in range(n)]

def prefix_sum(n,m):
    prefixSum = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefixSum[i][j] = prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]+graph[i-1][j-1]
    return prefixSum

prefixSum = prefix_sum(n,m)
for i in range(m):
    x1, y1, x2, y2 = (map(int, input().split()))
    #해당 합을 구하여 출력한다.
    result = 0

    # 이는 부분합에 더 가깝다.
    partSum = prefixSum[x2][y2]-prefixSum[x1-1][y2]-prefixSum[x2][y1-1]+prefixSum[x1-1][y1-1]
    print(partSum)


