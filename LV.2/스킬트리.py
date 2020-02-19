case = ["BACDE", "CBADF", "AECB", "BDA"]


def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:  # 각 유저의 스킬트리를 받아옴
        skill_list = list(skill)
        for s in skills:  # 해당 스킬트리의 스킬을 하나씩 검사
            if s in skill:  # 해당 스킬이 스킬트리 안에 있다면 추가 검사
                # 해당 스킬이 스킬트리의 첫번째 문자와 같지 않다면, 순서가 맞지 않으므로 break로 건너 뜀
                if s != skill_list.pop(0):
                    break
        else:  # 조건 검사 후에도 남은 경우 알맞은 스킬트리이므로 그때 answer의 값을 1증가
            answer += 1
    return answer  # 모든 조건을 다 확인한 이후 저장된 answer의 값을 정답으로 return


print(solution("CBD", case))
