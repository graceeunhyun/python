#정렬 문제인데 줄 서 있는 어린이중 한명을 선택하여 제일 앞이나 제일 뒤로 보낸다.
# 퀵정렬 문제로 이중에서 가장 count 를 작게 해서 보내는 문제
def partition(arr, low, high):
    global count
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            count += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    count += high - (i + 1)
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

n = int(input())
arr = list(map(int, input().split()))
count = 0
quicksort(arr, 0, n - 1)

print(count/2)

