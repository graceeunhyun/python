val = list(input())
answer = list(["U","C","P","C"])
visited=[0]*4

#해당 val 이 이제 UCPC 를 포함할수 잇으면 이제 해당 테스트를 통과하는 것으로 간주한다.
count= 0
for i in val:
    if i == answer[count]:

        count+=1

    if count == 4:
        break


if count ==4:
    print("I love UCPC")
else:
    print("I hate UCPC")
