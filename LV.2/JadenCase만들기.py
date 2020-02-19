# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# s는 길이 1 이상인 문자열입니다.
# s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
# 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )


def solution(s):  # 내가 푼 문제, 공백이 여러개인 경우 처리가 안되서 일부 케이스에서 실패 발생
    s = s.lower()
    s_list = s.split(" ")
    second_list = [i[1:] for i in s_list]
    first_char = []
    answer = []
    for string in s_list:
        if string[0].isalpha() == True:
            first_char.append(string[0].upper())
        else:
            first_char.append(string[0])
    for i in range(len(second_list)):
        answer.append(first_char[i]+second_list[i])

    return ' '.join(answer)


def solution2(s):
    s = s.lower()
    L = s.split(" ")
    answer = ""
    for i in L:
        i = i.capitalize()
        answer += i+" "
    return answer[:-1]


print(solution2("3people unFollowed me"))
