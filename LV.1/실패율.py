# 슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다.
# 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다.
# 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

# 이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다.
# 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다.
# 오렐리를 위해 실패율을 구하는 코드를 완성하라.

# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

# 제한사항
# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

# N의 길이만큼 실패율 저장 배열 failuare 생성
# stages배열을 돌면서 stages[i-1] == index(failuare[i+1])와 같다면 failuare[i]값 증가
# failuare 배열을 오름차순으로 정렬한 후 반환
case1 = [2, 1, 2, 6, 2, 4, 3, 3]
case2 = [4, 4, 4, 4, 4]


def solution(N, stages):  # 내가짠 코드 정상작동하나, 실패율이 같은 스테이지가 있는 경우 예외처리를 생각하지 못해서 실패
    tempAnswer = []
    failuare = [0]*N
    for i in range(len(stages)):
        ref = stages[i]-1
        if ref < N:
            failuare[ref] += 1
    for i in range(len(failuare)):
        # numberOfStage =
        stageCount = len(list(filter(lambda x: x > i, stages)))
        tempAnswer.append((failuare[i]/stageCount))
    answer = sorted(tempAnswer, reverse=True)
    result = []
    for i in answer:
        res = tempAnswer.index(i)
        if res == tempAnswer[int(i)]:
            result.append(tempAnswer.index(i)+2)
        else:
            result.append(tempAnswer.index(i)+1)
    return result


def best_solution(N, stages):  # 다른 사람의 풀이 중 가장 간결하고 효울성이 높은 코드
    result = {}  # 딕셔너리를 사용해서 실패율, 도전자 수를 함께 저장
    denominator = len(stages)  # 전체 도전자수에서 성공한 인원을 뺄 것이므로 stages 길이만큼 변수 생성
    for stage in range(1, N+1):  # (스테이지가 1부터 시작하므로 1 ~ N+1만큼 반복 진행)
        if denominator != 0:  # 남은 도전자수가 0이 아니면 실패율 검사 진행
            count = stages.count(stage)  # 스테이지를 클리어한 사람의 수를 count()로 구함
            # 인덱스/실패율을 딕셔너리에 저장 ex) 1 : 2 => 첫번째 스테이지에서 2명 실패
            result[stage] = count / denominator
            denominator -= count  # 해당 스테이지의 실패율 계산이 끝났으므로 전체 도전자에서 실패한 사람의 수만큼 차감
        else:  # stage 검사시 남은 도전자가 없다면 스테이지에 도달한 유저가 없다는 뜻이므로 0을 값으로 생성 ex) 10 : 0
            result[stage] = 0

    # 람다식으로 딕셔너리의 key를 가져오되, 값을 내림차순으로 정렬해서 리턴함
    return sorted(result, key=lambda x: result[x], reverse=True)
