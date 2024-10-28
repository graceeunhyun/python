n = int(input())
#해당 시간을 출력한다
aTime = 0 #1번이 이기는 시간
bTime = 0
flag = 0

for i in range(n):
    teamNo, time = input().split()
    m,s = map(int, time.split(':'))
    #누가 이기고 있었는지 확인
    if teamNo =="1":

        if flag ==0:
            #처음으로 이기는 것임
            aTime += (48*60)-(60*m+s)

        flag+=1
        if flag ==0:
            if bTime>0:
                bTime=bTime-(48*60 - (60*m+s))

    else:
        if flag ==0:
            bTime += (48*60)-(60*m+s)
        flag-=1

        if flag ==0:
            if aTime>0:
                aTime=aTime-(48*60 - (60*m+s))


print('{:0>2}:{:0>2}'.format(aTime//60,aTime%60))
print('{:0>2}:{:0>2}'.format(bTime//60,bTime%60))





