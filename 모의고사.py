# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, / 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, / 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.


def solution(answers):
    n = len(answers)
    stu1 = [1, 2, 3, 4, 5] * n  # 학생1 배열
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5, ] * n  # 학생2 배열
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * n  # 학생3 배열
    count = {1: 0, 2: 0, 3: 0}
    for i in range(0, n):
        if answers[i] == stu1[i]:
            count[1] += 1
        if answers[i] == stu2[i]:
            count[2] += 1
        if answers[i] == stu3[i]:
            count[3] += 1

    return [key for key, value in count.items() if value > 0]


def solution2(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)
    # q = 정답 배열의 인덱스, a = 각 인덱스의 값(정답 번호)
    for q, a in enumerate(answers):
        # i = 각 학생들의 인덱스 위치, v = 각 학생이 적은 답의 패턴 배열
        for i, v in enumerate(p):
            # 정답 번호 = 정답배열의 인덱스 % 학생별 정답 패턴의 길이 라면 ex) 정답번호 1 % 5 = '1'
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


answer1 = [1, 2, 3, 4, 5]
answer2 = [1, 3, 2, 4, 2]
# print(solution2(test2))
