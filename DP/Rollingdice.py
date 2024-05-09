n, m, r,c  = map(int, input().split())
direction = list(map(int, input().split()))
arr = [[0 for _ in range(n)] for _ in range(n) ]

# 주사위를 돌렸을 경우 어떻게 변하는지 확인
# def rollingDice(direction):
#
#
#
# for i in range(m):
#     rollingDice(direction[i])