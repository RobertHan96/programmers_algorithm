# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

Arr1 = [[1, 4], [3, 2], [4, 1]]
Arr2 = [[3, 3], [3, 3]]


def solution(arr1, arr2):
    answer = []
    for idx1 in range(len(arr1)):
        row = []
        for idx2 in range(len(arr2[0])):
            tmp = 0
            for idx3 in range(len(arr1[0])):
                tmp += arr1[idx1][idx3] * arr2[idx3][idx2]
            row.append(tmp)
        answer.append(row)
    return answer
