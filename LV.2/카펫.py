# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 빨간색으로 칠해져 있고 모서리는 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
# Leo는 집으로 돌아와서 아까 본 카펫의 빨간색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
# Leo가 본 카펫에서 갈색 격자의 수 brown, 빨간색 격자의 수 red가 매개변수로 주어질 때
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.


def solution(brown, red):
    answer = []
    n = brown + red
    for i in range(1, n+1):
        if i * (i+1) == n:
            answer.append(i)
            answer.append(i+1)
    answer.sort(reverse=True)
    return answer


print(solution(8, 1))

# 두개의 파라미터를 더한수의 공배수가 정답임
# 가로길이 >= 세로길이 이므로 공배수를 구해서, 큰 값을 앞에 넣어서 리턴
