# 1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.
# 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)


def solution(board):
    width = len(board[0])
    height = len(board)
    for i in range(1, height):  # 격자의 대각선 마지막 값이 최종 해답이므로 0번이 아닌 1번째 인덱스부터 검사 시작
        for j in range(1, width):
            if board[i][j] == 1:  # 만약 해당 좌표의 값이 1이라면
                board[i][j] = min(  # 대각선 왼쪽, 같은행의 왼쪽, 윗행의 값 중 가장 작은값에 1을 더함
                    board[i-1][j-1], min(board[i-1][j], board[i][j-1])) + 1
                # 이렇게 전체 배열을 확인하면 마지막행, 마지막열의 값이 연속된 점의 개수 만큼 할당됨
                # 배열의 가장 큰 값을 가져오고 제곱을 구하면 사각형의 넓이를 구할 수 있음
    return max([item for row in board for item in row]) ** 2


case1 = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
case2 = [[0, 0, 1, 1], [1, 1, 1, 1]]

print(solution(case1))
