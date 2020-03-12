# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 빨간색으로 칠해져 있고 모서리는 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
# Leo는 집으로 돌아와서 아까 본 카펫의 빨간색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
# Leo가 본 카펫에서 갈색 격자의 수 brown, 빨간색 격자의 수 red가 매개변수로 주어질 때
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 아래와 같이 접근했으나, 예외케이스에서 실패가 발생하여, 정답을 구글링 한 후 진행
# 두개의 파라미터를 더한수의 공배수가 정답임
# 가로길이 >= 세로길이 이므로 공배수를 구해서, 큰 값을 앞에 넣어서 리턴


def solution(brown, red):
    answer = []
    n = brown + red
    for i in range(1, n):
        if i * (i+1) == n:
            answer.append(i)
            answer.append(i+1)
    answer.sort(reverse=True)
    return answer

# 구글링을 통해 찾은 간결한 해결 방법
# brown : 8 , red : 1 일때의 예시


def best_solution(brown, red):  # 빨간색 부분의 길이만 알면 빨간색 가로+2, 세로+2가 전체 길이이므로 빨간색의 크기를 구해야함
    for index in range(1, red+1):  # 1 ~ red+1 범위 동안 검사하면서 빨간색의 길이를 구함
        if red % index == 0:  # ex) 1 % 1 == 0 이므로 빨간색의 길이는 1임
            length = red//index  # 이때 red의 가로+2 * 세로 +2 값이 brwon과 같다면 해당 값을 통해 전체 길이를 구할 수 있음
            # ex)(1+2)*(1+2)-(1*1) = brown(8) -> 8 = 8
            if (((index+2)*(length+2))-(index*length)) == brown:
                # 가로가 항상 긴 사각형이므로, 좌표 값 중 큰 값을 가로, 작은 값을 세로로 리턴
                return [max(index+2, length+2), min(index+2, length+2)]
