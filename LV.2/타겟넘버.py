# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

from itertools import product

test = [1, 1, 1, 1, 1]


def iter_solution(numbers, target):  # 파이써닉하게 해결한 솔루션
    l = [(x, -x) for x in numbers]
    print()
    s = list(map(sum, product(*l)))
    print(s)
    return s.count(target)


print(iter_solution(test, 3))


def solution(numbers, target):
    # result_list는 0부터 시작한다. 그리고, [0, 0-a, 0+a, 0-a-b, 0-a+b, 0+a-b, 0+a+b, ... ] 이런 식으로 간다.
    result_list = [0]

    # i는 numbers의 각 원소들, numbers의 개수 만큼 노드의 깊이가 결정되므로 해당 값을 이용
    for i in range(len(numbers)):
        # 각 노드 레벨에 진입할때마다 temp_list를 생성한다, 여기에 해당 레벨의 자식노드 들을 + 혹은 - 한 값들을 더해나간다.
        temp_list = []

        # result_list는 0부터 numbers의 각 원소들을 빼고 더한 값들이 있다.
        for j in range(len(result_list)):
            # 부모 노드에서 본인(i)의 값을 빼거나 더하면 경우의 수를 모두 구해나갈 수 있다.
            temp_list.append(result_list[j] - numbers[i])
            temp_list.append(result_list[j] + numbers[i])
            print("루트노드에서 -한 값", result_list[j] - numbers[i])
            print("루트노드에서 +한 값", result_list[j] + numbers[i])

        # 그래프의 마지막 레벨에서 수행한 결과를 최 종 결과로 반환
        result_list = temp_list
        print(result_list)
    # 반환된 배열 값 중 찾고자하는 숫자와 일치하는 값의 개수를 count해서 최종답 반환
    return result_list.count(target)
