import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    pq = []
    lq = []
    deleted = set()
    for _ in range(k):
        val = input().split()
        if val[0] == 'I':
            num = int(val[1])
            heapq.heappush(pq, num) #최소값
            heapq.heappush(lq, -num) #최대값
        elif val[0] == 'D':
            if not pq:
                continue
            if val[1] == '1':
                deleted.add(-heapq.heappop(lq))  # 삭제된 값을 추가합니다. #최대값
            else:
                deleted.add(heapq.heappop(pq))  # 최대 우선순위 큐에서 삭제된 값을 추가합니다. / 최소값

    # 삭제된 값들을 우선순위 큐에서 제거합니다.
    pq = [-x for x in pq if x not in deleted]
    lq = [x for x in lq if x not in deleted]
    print(pq)
    print(lq)
    if not pq or not lq:
        print("EMPTY")
    else:
        print(-lq[0], pq[0])  # 최대값과 최소값을 출력합니다.
