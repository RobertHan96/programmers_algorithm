# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때,
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
z
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

# 내가 푼 함수, 일부 테스트케이스를 통과하지 못함, 두 좌표간의 거리를 구할때 피타고라스 정리로는 누락이 발생하는 것으로 추정


def my_solution(numbers, hand):
    answer = ''
    hand_standfor = ''
    if hand == 'right':
        hand_standfor = 'R'
    else:
        hand_standfor = 'L'

    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              ['*', 0, '#']
              ]
    numbers_for_left_hand = [1, 4, 7]
    numbers_for_right_hand = [3, 6, 9]
    pressed_numbers_leftside = ['*']
    pressed_numbers_rightside = ['#']

    for num in numbers:
        if num in numbers_for_left_hand:
            answer += 'L'
            pressed_numbers_leftside.append(num)
        elif num in numbers_for_right_hand:
            answer += 'R'
            pressed_numbers_rightside.append(num)
        else:
            result = find_side(
                keypad, pressed_numbers_leftside[-1], pressed_numbers_rightside[-1], num, hand_standfor)
            if result == 'L':
                answer += 'L'
                pressed_numbers_leftside.append(num)
            else:
                answer += 'R'
                pressed_numbers_rightside.append(num)
    print(answer)
    return answer


def find_side(keypad, left_number, right_number, target_number, hand):
    left_index = (0, 0)
    right_index = (0, 0)
    target_index = (0, 0)
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == target_number:
                target_index = (i, j)
            elif keypad[i][j] == right_number:
                right_index = (i, j)
            elif keypad[i][j] == left_number:
                left_index = (i, j)
    leftX = target_index[0] - left_index[0]
    leftY = target_index[1] - left_index[1]
    left = math.sqrt((leftX*leftX)+(leftY*leftY))

    rightX = target_index[0] - right_index[0]
    rightY = target_index[1] - right_index[1]
    right = math.sqrt((rightX*rightX)+(rightY*rightY))

    if left < right:
        return 'L'
    elif left == right:
        return hand
    else:
        return 'R'


# 딕셔너리(해시)를 이용해 더 단순화한 해결 코드, 다른 사람의 풀이 중 가장 많이 사용된 예제
def get_distance(hand, number):
    # 좌표 개수가 많지 않으므로 딕셔너리 형태로 미리 키:밸류 형태의 좌표를 미리 생성해서 거리를 쉽게 구함
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    number = str(number)
    x_hand, y_hand = location[hand]
    x_number, y_number = location[number]
    return abs(x_hand - x_number) + abs(y_hand - y_number)


def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    hand = 'R' if hand == 'right' else 'L'
    # 왼쪽, 오른쪽, 가운데 줄의 숫자인지 여부에 따라 비교하는 로직, 내가 작성한 것과 거의 동일
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = str(number)
            continue
        if number in [3, 6, 9]:
            answer += 'R'
            right = str(number)
            continue
        if number in [2, 5, 8, 0]:
            dis1 = get_distance(left, number)
            dis2 = get_distance(right, number)
            if dis1 > dis2:
                answer += 'R'
                right = str(number)
            if dis1 < dis2:
                answer += 'L'
                left = str(number)
            if dis1 == dis2:
                answer += hand
                if hand == 'R':
                    right = str(number)
                if hand == 'L':
                    left = str(number)
    return answer


solution(nums, hand)
