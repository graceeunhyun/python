n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]
print(first, second)
result = 0

# 횟수를 계산
count = int (m/k+1)*k
# 안나눠지는 경우도 포함
count += m%(k+1)

result += (count)* first
result += (m-count)*second
print(result)

