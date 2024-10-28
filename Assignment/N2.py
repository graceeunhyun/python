import heapq
heap = []

n = int(input())
for _ in range(n):
    numbers = map(int, input().split())
    #메모리 이슈가 있기 때문에 바로바로 해당 heap 의 크기를 유지
    for number in numbers:
        if len(heap) < n:
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)

print(heap[0])
