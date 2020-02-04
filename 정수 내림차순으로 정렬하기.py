# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.


def solution(n):
    # n을 문자열로 변환 => 각 문자를 list형태로 저장
    # 저장된 리스트를 내림차순으로 정렬 => join()함수로 리스트내 문자 결합
    # 최종적으로 결합된 문자열을 다시 int형으로 변환
    return int(''.join(list(sorted(str(n), reverse=True))))


print(solution(118372))
