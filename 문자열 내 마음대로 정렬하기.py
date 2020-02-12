# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때,
# 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
# 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.

# 제한 조건
# strings는 길이 1 이상, 50이하인 배열입니다.
# strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
# strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
# 모든 strings의 원소의 길이는 n보다 큽니다.
# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
# 입출력 예) [sun, bed, car] =>	1 => [u,e,a] => [car, bed, sun]

case1 = ['sun', 'bed', 'car']
case2 = ['abzcd', 'cdzab', 'abzfg', 'abzaa', 'abzbb', 'bbzaa']

# n+1이후 문자열만 비교하면 됨

# sorted 함수를 두번 중첩해서 사용해도 정상 사용됨


def solution(strings, n):
    return sorted(sorted(strings), key=lambda i: i[n])


print(solution(case1, 1))
