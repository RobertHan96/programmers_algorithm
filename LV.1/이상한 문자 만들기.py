# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

# 공백 단위로 문장 나누기
# 각 단어의 0 or 짝수번째 인덱스 같은 upper()함수로 변환, 아니라면 lower()함수로 변환
# 변환된 배열을 join()으로 결합하여 리턴


def solution(s):  # 내가 구현한 해결 함수
    answer = s.split(' ')
    text = ''
    for i in range(len(answer)):
        count = 0
        word = answer[i]
        for j in range(len(word)):
            if j % 2 == 0 or j == 0:
                text += word[j].upper()
            else:
                text += word[j].lower()
            count += 1
        if count == len(word):
            text += ' '
            # 문자열의 끝에도 공백이 올수 있다는 것을 생각하지 못해서 일부 TC 수행 실패
    return text.rstrip()

# enumerate()로 값,인덱스를 한번에 얻을수 있기 때문에 쉽게 해결 가능


def best_solution(s):
    word_list = []
    for i, x in enumerate(s.split(" ")):
        print(i, ":", x)
    # s.split(" ") : 공백을 기준으로 인덱스, 값을 얻게됨 아래와 같이 정렬됨
        # 0 :
        # 1 :
        # 2 : try
        # 3 : hello
        # 4 : world
    for word in s.split(" "):
        # enum을 이용해 각 단어의 문자, 인덱스를 가져와 짝/홀 여부를 판단하고, 대/문자로 변환하는 컴프리헨션
        # 공백이라면 대/소문자 변경이 안되므로, 공백이 그대로 반환됨
        word = "".join(x.lower() if i % 2 else x.upper()
                       for i, x in enumerate(word))
        # 하나의 글자에 대한 대/소문자 변환이 끝났다면 최종 결과 리스트에 추가
        word_list.append(word)
    return " ".join(word_list)  # 리스트의 값을 공백을 기준으로 합치면 최종 정답 완성
