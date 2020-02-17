# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

test = 'Zbcdefg'


def solution(s):  # 내가 짠 코드
    answer = ''
    uppers = []
    lowers = []
    for i in s:
        if ord(i) < 97:
            uppers.append(ord(i))
        else:
            lowers.append(ord(i))
    lowers.sort(reverse=True)
    uppers.sort(reverse=True)
    for i in lowers:
        answer += chr(i)
    for i in uppers:
        answer += chr(i)
    return answer


def solution2(s):  # 한줄로 구현된 베스트 코드
    return ''.join(sorted(s, reverse=True))
