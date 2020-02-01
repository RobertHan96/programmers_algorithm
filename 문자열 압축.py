# s를 2~n-1 단위로 나눈 경우와 s의 길이를 순차 비교
# 비교 결과를 저장할 임시 변수 생성
# 반복문을 다 돌았을때 임시 변수와 s의 길이 비교
# s가 더 길면 임시 변수 값을 리턴하고, 아니라면 s의 길이를 리턴


def solution(s):
    # 1 ~ n-1 단위로 압축한 문자열을 담아서 비교하기 위한 배열 생성
    answers = []
    # 만약 입력된 문자열의 길이가 1이면 압축할 필요가 없으므로 1을 정답으로 리턴
    if len(s) == 1:
        return 1
    # 1~ n-1까지 반복하면서 압축된 문자열 얻기 (0번째 인덱스는 비교할 필요가 없으므로 1부터 시작)
    for i in range(1, len(s)):
        answer = ''  # 임시의 빈 문자열 할당
        count = 1  # 처음에는 1개 단위로 문자열을 압축할 것이므로 1 할당
        # 1 ~ n-1까지, 상위 반복문의 인덱스 i의 step만큼 문자열 검사
        for j in range(i, len(s), i):
            # 1회차 예시 : s[0:1]이 s[1:2]와 같을 경우 count 1 증가
            if s[j-i:j] == s[j:j+i]:
                count += 1
            # 앞,뒤 문자열이 같지 않다면 압축할 수 없는 경우이므로 answer에 문자열 추가
            else:
                # 이때 count가 1이라면 압축이 불가한 경우이므로 앞 문자열에 해당하는 s[0:1]을 그대로 answer에 추가
                if count == 1:
                    answer += s[j-i:j]
                # count가 1이 아니라면 압축된 경우이므로, count수를 문자열로 바꿔서 answer에 추가
                else:
                    answer += str(count)+s[j-i:j]
                    # 답을 추가했다면 다음 문자열 검사시 겹치지 않기위해 count값을 1로 재할당
                    count = 1
        # 이중 반복문의 인덱스j와 i의 값이 같다면 해당 단위의 문자열 압축 경우를 다 시도한 것이므로
        # answer의 값을 확인한 후 answers에 추가
        if len(s[j:j+i]) == i:
            # 이때 count 값이 1이라면 압축되지 않은 경우이므로 answer에 그대로 string 추가
            if count == 1:
                answer += s[j-i:j]
            # count값이 1이 아니라면 압축된 경우이므로 count + string 추가
            else:
                answer += str(count)+s[j-i:j]
                # 답을 추가했다면 다음 문자열 검사시 겹치지 않기위해 count값을 1로 재할당
                count = 1
        else:
            # i, j의 같이 같지않을때, 즉 문자열이 하나만 남아서 압축이 불가능한 경우 answer 그대로 string 추가
            answer += s[j:j+i]
        # 이중 for문, if문으로 모두 걸른 answer가 최종 값이므로 answer배열에 answer의 lenth값 추가
        answers.append(len(answer))
        # answer 배열 중 가장 짧은 값이 최종 정답이므로 min 함수를 이용해서 최종 정답 리턴
        print(answer, answers)
    return min(answers)


test = "aabbaccc"

print(solution(test))

# 프로그래머스 제출 답변 중 가장 가독성이 좋고 정답자수가 많은 코드


def solution2(s):
    answer = len(s)  # 입력받은 문자열의 길이를 바로 정답으로 지정
    # 입력받은 s/2 보다 길이가 긴 경우 문자열 압축이 안된 것이므로 n/2+1 인덱스까지만 반복문 진행
    for x in range(1, int(len(s)/2)+1):
        d = 0
        # 이전 문자열 vs 문자열+x가 같은지 비교하기 위한 임시 변수 comp 생성
        comp = ''
        # 앞의 문자열의 중복 횟수를 표시하기 위한 count 변수 생성
        c = 1
        # 입력된 문자열의 0번 ~ 끝까지 x 단위로 체크 진행
        for i in range(0, len(s), x):
            # 0~1번자 문자열 지정
            temp = s[i:i+x]
            # 앞의 문자열과, 뒤의 문자열이 같다면 count 1증가
            if comp == temp:
                c += 1
            # 앞의 문자열과 뒤 문자열이 같지 않다면 다음에 비교할 문자열의 길이를 temp만큼 증가
            elif comp != temp:
                d += len(temp)
                # 이때 count가 1 이하라면
                if c > 1:
                    d += len("{}".format(c))
                c = 1
                comp = temp
        if c > 1:
            d += len("{}".format(c))
        answer = min(answer, d)
    return answer
