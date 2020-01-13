# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# 예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.
# 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때,
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

test = [2, 1, 3, 2]


def solution(p, l):
    answer = 0
    maxValue = max(p)
    while True:
        # 리스트의 첫 요소부터 값을 비교하기 위해 첫번째요소 값을 임시저장하는 변수 v 생성
        v = p.pop(0)
        # 첫 요소 값이 배열에서 가장 크다면, 값을 뽑아서 배열 맨뒤에 추가
        if maxValue == v:
            answer += 1
            # 더 이상 비교할 값이 없으면 while 반복문 중단
            if l == 0:
                break
            else:
                l -= 1
            maxValue = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return answer


result = solution(test, 1)
print("계산 결과 출력 순서 : {}".format(result))
