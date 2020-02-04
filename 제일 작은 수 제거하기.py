# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.


def solution(arr):
    smallest = min(arr)
    if len(arr) == 1:
        return [-1]  # 입력받은 arr의 값이 하나라면 내용을 확인할 필요가 없으므로 -1 리턴
    for i in arr:
        if i == smallest:  # 가장 작은 값과 인덱스 값이 같다면
            arr.remove(i)  # 해당 값을 제거하고, 바로 정답 리턴 (가장 작은 값이 여러개 있을수 있기 때문)
            return arr
    return arr  # 코드 모두 진행 후 예외 상황을 대비해 arr을 그대로 리턴 (같은 값만 있는 경우 [0,0,0])


def rm_small(mylist):
    # 함수를 완성하세요
    mylist.pop(mylist.index(min(mylist)))
    return mylist


case1 = [4, 3, 2, 1, 1, 1, 1]
