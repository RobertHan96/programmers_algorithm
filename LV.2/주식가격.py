# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
test = [1, 2, 3, 2, 3]

# 가격을 저장할 배열을 만들고, 각 시점에 해당 인덱스 위치에 가격을 저장한다, 반복문 1회로 끝내야 함


def solution(prices):
    answer = [0] * len(prices)
    # 마지막 값은 항상 0초에 해당하기 때문에 len-1 까지만 검사하면 됨
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer


print(solution(test))
