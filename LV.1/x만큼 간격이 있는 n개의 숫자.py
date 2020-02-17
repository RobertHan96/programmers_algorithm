# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.


def solution(x, n):
    if x == 0:  # 시작값, step이 0이면 range 함수 사용시 에러가 발생하므로 [0] * n 값을 정답으로 리턴
        return [0]*n
    # 시작값이 0이 아니라면 x부터 x*(n+1)까지 만큼 배열을 만들어 리턴하면됨
    return [i for i in range(x, x*(n+1), x)]


def solution2(x, n):
    # 베스트 풀이 : i*x+x를 시작 값으로하면 step,이나 별도의 if문 없이 구현 가능 , 시작 값이 0인 경우도 대응됨(곱셉이므로)
    return [i * x + x for i in range(n)]
