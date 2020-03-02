# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.


def isPrime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def solution(numbers):
    from itertools import chain
    from itertools import permutations
    answer = 0
    cb_list = []
    n_list = []
    for i in range(1, len(numbers)+1):
        cb_list.append(list(permutations(numbers, i)))
    temp_list = list(chain(*cb_list))
    for t in temp_list:
        n_list.append((int(''.join(t))))
    n_list = list(set(n_list))
    for num in n_list:
        if isPrime(num) == True:
            answer += 1

    return answer


print(solution('011'))
