# n : 배열의 크기
n = int(input())
#1차원 배열 B 에 넣엇을 경우에 B 를 오름차순 했을 때 B[k] 를 구해보자
k = int(input())

#print(n, k)
# 2 차원 배열 : A
# 해당 k 번째 수를 찾기 위해서 binary search 로 진행한다
start = 1
end = n * n
result = 0

# arr[i][j] = i*j
# 다돌려보니깐 메모리 에러나더라고

# binary search
# 3 7
# 1(1*1) 2(1*2) 3(1*3)
# 2(2*1) 4(2*2) 6(2*3)
# 3(3*1) 6(3*2) 9(3*3)

# sorting 된 상태 - k
# b[k] = 1 2 2 3 3 4 6 6 9
# x : 행
# i : 열


def count_less_equal(x):
    count = 0
    for i in range(1, n + 1):
        count += min(x // i, n)
    return count


while start < end:
    mid = (start + end) // 2

    # 해당 행에 있는 특정한 x 이하의 배열 원소 개수를 세는 함수
    if count_less_equal(mid) < k:
        start = mid + 1
    else:
        end = mid

print(start)
