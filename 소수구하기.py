# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)


def solution(n):
    # 짝수는 소수가 아니므로, 3~n까지 홀수값만 있는 배열 생성
    numbers = set([i for i in range(3, n+1, 2)])
    for i in range(3, n+1, 2):
        if i in numbers:
            # 특정수의 배수는 나누어지는 수가 있는 것이므로 해당 숫자를 배열을 돌면서 해당 배수 삭제
            numbers -= set([i for i in range(i*2, n+1, i)])
    # 배열생성시 3부터 시작했으므로 가장 작은 소수인 2는 제외됨, 따라 +1을 하여 최종적인 소수의 개수 완성
    answer = len(numbers)+1
    return answer
