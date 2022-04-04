# 시작 단어가 주어졌을때 목표 단어로 변경될때까지 걸리는 횟수를 반환하시오.
# 한번에 알파벳 하나씩만 바꿀 수 있고, 단어리스트에 정답이 없으면 0을 리턴하시오.
# Ex) hit => cog, [hot, dot, dog, lot, log, cog]일때 정답은 4

test = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

# 문제 의도(BFS)를 가장 잘 파악해서 재귀함수로 구현한 정답을 카피함
min_ = 51


def dfs(now, target, words, history=[], depth=0):
    global min_  # 입력값이 최대 50까지이므로 51을 할당한 후 재귀함수 실행
    print(now, history)
    if now == target:
        min_ = min(min_, depth)

    if depth >= min_:
        return

    for word in words:
        if word in history:
            continue
        cnt = 0
        for i in range(len(target)):
            if word[i] != now[i]:
                cnt += 1
            if cnt > 1:
                break
        if cnt == 1 and word not in history:
            history.append(word)
            dfs(word, target, words, history, depth+1)
            history.pop(-1)


def solution(begin, target, words):
    global min_
    if target not in words:
        return 0
    dfs(begin, target, words)
    return min_
