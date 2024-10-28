import sys

# 포켓몬의 개수: n
# 내가 맞춰야하는 문제의 갯수 : m
n, m = map(int, sys.stdin.readline().split())

# 문제는 이제 hash map 으로 어떻게 이제 해당 내용을 받고 이제 m 개의 문제의 수를 맞추면 되는 것임.
poketMon ={}
number_to_name={}
for i in range(n):
    name = sys.stdin.readline().rstrip()
    #이렇게 dictionary 형태로 내용물을 집어넣음
    poketMon[name] = i+1
    number_to_name[i+1] = name

for i in range(m):
    question =sys.stdin.readline().rstrip()
    if question.isdigit():
        #입력이 숫자인 경우, 번호로 검색
        print(number_to_name.get(int(question)))
    else:
        # 입력이 문자인 경우, 이름으로 검색
        print(poketMon.get(question))
