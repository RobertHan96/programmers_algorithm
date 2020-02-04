# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.


def solution(n):
    # 배열에서 [::-1]을 하면 해당 배열의 순서를 반대로 뒤집음
    return list(map(lambda i: int(i), (str(n)[::-1])))


print(solution(1241))
