import sys
n = int(sys.stdin.readline())
#집은 빨강, 초롱, 파랑색으로 치래야하고 아래 규칙을 만족해서 진행해야함.
role = ['R', 'G', 'B']
#이제 해당 집을 칠하는 비용을 받아야함.
arr = []
for i in range(n):
    val = list(map(int, sys.stdin.readline().split()))
    arr.append(val)

#해당 부분은 이제 각 각 칠하는 비용으로
dp = [[0 for _ in range(3)] for _ in range(n)]



#모든 집을 칠하는 비용의 최솟값