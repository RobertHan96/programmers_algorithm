# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.


def solution(n):
    import math  # 제곱근을 구하는 sqrt() 사용을 위해 모듈 임포트
    if int(math.sqrt(n)) == math.sqrt(n):  # 양의 정수라면 int()한 값과 안한 값이 같으므로 해당 조건으로 검사
        return (int(math.sqrt(n))+1) ** 2
    return -1


print(solution(11))
