n = int(input())
data = list(map(int, input().split()))

data.sort()
result = 1
for i in range(n):
   if result < data[i]:
       break
   result += data[i]



print(result)