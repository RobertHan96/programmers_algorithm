# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
s = "bc"
n = 3


def solution(s, n):
    answer = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                answer += chr((ord(i) - ord("a") + n) % 26 + ord("a"))
            else:
                answer += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
        else:
            answer += i
    return answer


print(solution(s, n))
