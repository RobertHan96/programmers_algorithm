# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
s = "AB"
n = 1


def solution(s, n):
    stringArrary = []
    resultArrary = []
    answer = ""

    for i in s:
        i = ord(i)
        if i == 32:
            stringArrary.append(ord(" "))
        elif i == 90:
            stringArrary.append(ord("A")+n-1)
        elif i == 122:
            stringArrary.append(ord("a")+n-1)
        else:
            stringArrary.append(i+n)
    for j in stringArrary:
        resultArrary.append(chr(j))
    for char in resultArrary:
        answer = answer + char
    return answer


solution(s, n)
