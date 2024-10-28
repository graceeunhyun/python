n = int(input())
m = int(input())

# 버스의 정보를 받아서 정렬한다
# 플로이드 워셜 알고리즘을 사용한다.
# 모든 정점에서 다른 모든 정점으로 가는 최소 비용을 구한다

# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화한다
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화한다
for i in range(1, n+1):
    for j in range(1, n+1):
        if i== j:
            graph[i][j] = 0


# 간선의 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용은 c
    if c< graph[a][b]:
        graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == int(1e9):
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()