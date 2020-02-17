# n	5
# arr1	[9, 20, 28, 18, 11]
# arr2	[30, 1, 21, 17, 28]
# 출력	["#####","# # #", "### #", "# ##", "#####"]

# 1) 입력받은 배열을 2진수로 변환해서 저장
# 2) 2진수에서 1은 #으로, 0은 공백으로 변환
# 3) 배열1과 배열2를 #으로 변환한 값을 더해서 출력

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = format(arr1[i] | arr2[i], str(n)+'b')
        temp = temp.replace('0', ' ')
        temp = temp.replace('1', '#')
        answer.append(temp)
    return answer
