# 탐욕 알고리즘의 기초와 같은 문제
# 지불해야할 거스름돈 금액이 주어졌을때 동전개수를 가장 적게 쓰면서 지불할때 필요한 동전의 개수를 출력하시오
# 동전은 10원, 50원, 100원, 500원권만 있다고 가정함


def change(amount):
    answer = 0
    remains = 0
    if amount >= 100:
        remains = amount % 100
        answer = amount // 100
        if amount < 100:
            remains = remains % 50
            answer = answer + remains // 50
    return answer


print(change(350))
