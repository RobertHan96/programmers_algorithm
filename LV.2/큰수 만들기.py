# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.


def solution(number, k):
    # 1. 스택 생성
    st = []

    # 2. 큰 수가 앞자리가 되게끔 스택에 저장합니다.
    for elem in number:
        while st and st[-1] < elem and k > 0:
            st.pop()
            k -= 1

        st.append(elem)

    # 3. k가 남았다면 뒤에서부터 뺍니다.
    while k > 0:
        st.pop()
        k -= 1

    answer = "".join(st)
    return answer


print(solution('1924', 1))

# 가장 간결하고 풀이가 많은 함수
def best_solution(number, k):
    stack = [number[0]] #
    for num in number[1:]: # 문자열길이 만큼 검사하고, 문자의 위치가 바뀔때마다 k-1을 하므로, k >0을 종료조건으로 while 진행
        while len(stack) > 0 and stack[-1] < num and k > 0: 
            k -= 1
            stack.pop() # 숫자의 순서가 바뀔 경우라면, 즉 앞의 수보다 작다면 stack에서 제거하고 k를 1감소
        stack.append(num) # 아니라면 그대로 stack에 문자 추가
    if k != 0: # 위에서 검사가 다끝나면 큰 순서대로 stack 저장된 상태임, 이때 k != 0이라면 문자길이가 길기 때문에 슬라이싱 진행
        stack = stack[:-k] # -k 만큼 뒤에 남은 문자를 잘라줌
    return ''.join(stack) # stack남은 최종 정답을 join으로 묶어서 결과로 반환
