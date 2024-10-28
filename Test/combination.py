import itertools
#로또 번호 생성
#로또 번호 생성: 로또 번호는 1부터 45까지의 숫자 중 6개를 선택하는 것입니다. 이는 45개의 숫자 중에서 6개를 선택하는 조합 문제로 볼 수 있습니다. 이때, 선택된 숫자들의 순서는 중요하지 않으므로 조합을 사용합니다.
def generate_lotto_numbers():
    numbers = range(1, 46)
    lotto_numbers = list(itertools.combinations(numbers, 6))
    return lotto_numbers

lotto_numbers = generate_lotto_numbers()
# for numbers in lotto_numbers:
#     print(numbers)
#array 형태로 나오니 실제 count 를 구하려면 아래와 같이 구할 수가 있다.
print(len(lotto_numbers))
