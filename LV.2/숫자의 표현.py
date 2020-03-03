# Finn은 요즘 수학공부에 빠져 있습니다.
# 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
# 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15

# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.


def solution(n):
    answer = 0
    # 입력받은 수의 절반 이상에 해당하는 수는 연속해서 표현할 수 없으므로 n//2+2까지 숫자만 확인
    numbers = range(1, n//2+2)
    for i in numbers:
        sum = 0
        for j in range(i, n//2+2):
            sum += j
            if sum == n:
                answer += 1
            elif sum > n:  # sum이 입력받은 수(n)보다 크면 더 확인할 필요가 없으므로 break
                break
    answer += 1  # 항상 자기 자신은 포함되므로 마지막에 카운트1 증가
    return answer


print(solution(15))
