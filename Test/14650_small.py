import itertools
n =int(input())
num = [0,1,2]
count = 0
#0,1,2의 조합을 만들어서 n자리 3의 배수인지 확인하여 배수 개수를 세어준다
if(n ==1 ):
    print(0)
else:
    for j in itertools.product(num, repeat=n):
        if(j[0] == 0):
            continue

        if sum(j) % 3 == 0:
            count += 1
    print(count)