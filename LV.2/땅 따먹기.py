test = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]


def mySolution(land):
    answer = 0
    index = land[0].index(max(land[0]))
    answer += max(land[0])
    for i in range(1, len(land)):
        temp = [i for i in land[i]]
        temp_max = max(temp)
        if temp.index(temp_max) == index:
            temp.remove(temp_max)
            temp_max = max(temp)
            answer += temp_max
        else:
            answer += temp_max
            index = temp.index(temp_max)

    return answer


def solution(land):
    answer = 0
    N = len(land)  # N은 행의 개수가 된다.

    # i+1번째 행에 0번째 열에는 i번째 행에 1,2,3 열 중 최대값을 더해준다.
    # 즉 자신과 같은열에 있는 값을 제외한 값 중 최대값을 매행에 더해나간다. (DP 테이블과 유사한 개념)
    for i in range(0, N-1):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])

    # 바로 위에 코드가 똑같은 코드다. N-1행에서의 최대값을 가지는 열 answer에 대입한다.
    answer = max(land[N-1])
    return answer


print(solution(test))
