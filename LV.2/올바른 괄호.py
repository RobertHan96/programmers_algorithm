# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# ()() 또는 (())() 는 올바른 괄호입니다.
# )()( 또는 (()( 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# (와 )의 개수가 맞는지 검사
# 맞다면 앞에서부터 올바른 순서로 괄호가 나왔는지 검사


def solution(s):
    answer = False
    front_bracket = 0
    if s[0] == ")":
        return False
    for bracket in s:
        if bracket == "(":
            front_bracket += 1
        else:
            front_bracket -= 1
        if front_bracket < 0:
            break
    if front_bracket == 0:
        answer = True
    return answer


def is_pair(s):  # 스택과 에러처리(Try문)을 통해 구현한 예시, 가장 깔끔한 것으로 생각됨
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False
    return len(st) == 0  # 배열의 길이가 0과 같다면 True를 아니라면 False를 리턴
