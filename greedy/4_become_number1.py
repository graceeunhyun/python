n, k = map(int, input().split())
count = 0
while True:
    if n ==1:
        break

    if n%k ==0:
        n = (int)(n//k)
        count+=1
    else:
        n-=1
        count+=1

    # if n<k:
    #     break


print(count)