
# 내가 푼 풀이, 일부 케이스에서 시간초과 떠서 실패
from collections import OrderedDict


def mySolution(s):
    temp = ''
    nums = []

    for i in s[1:-1]:
        if i.isnumeric():
            temp += i
        elif i == ',':
            nums.append(int(temp))
            temp = ''
    nums.append(int(temp))
    answer = sorted(nums, key=lambda x: nums.count(x), reverse=True)

    return list(OrderedDict.fromkeys(answer))

# 실제로 통과한 다른 사람의 풀이


def solution(s):
    s = s[2:-2].split("},{")
    sorted_s = sorted(s, key=lambda x: len(x))
    answer = []
    check = set()
    for value in sorted_s:
        for each_value in value.split(","):
            if each_value not in check:
                answer.append(int(each_value))
                check.add(each_value)
                break
    return answer
