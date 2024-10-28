n = int(input())
arr = list(map(int, input().split()))

#무게를 사용해서 측정할 수 없는 양의 정수 무게 중 최솟값을 출력한다
arr.sort()
answer = 1

for i in range(n):

    if answer < arr[i]:
        break
    answer += arr[i]

print(answer)