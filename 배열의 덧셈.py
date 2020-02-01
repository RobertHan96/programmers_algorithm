# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.


def solution(arrInput1, arrInput2):
    answer = []
    for i in range(len(arrInput1)):
        # 리턴 형식이 값 행,열의 값을 더한 리스트이므로 임시 저장용 배열 생성
        temp = []
        for j in range(len(arrInput1[i])):
            # 입력받은 2개 리스트의 행, 열 인덱스를 가져와서 더함
            temp.append(arrInput1[i][j] + arrInput2[i][j])
        # 임시로 만든 덧셈 리스트를 최종 리턴배열에 더함
        answer.append(temp)
    return answer


arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
arr3 = [[1], [2]]
arr4 = [[3], [4]]
print(solution(arr1, arr2))
