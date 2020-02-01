# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.


# 커맨드의 기준값을 기준으로 반복문을 돌릴 임시 배열을 만든다
# 해당 배열을 sort함수로 정렬한다 (함수 자체를 정렬)
# 정렬된 함수의 커맨드 배열에서 k를 가져와 임시 배열의 k번째 인덱스를 뽑는다
# 뽑은 값을 answer 배열에 추가한다

myArrary = [1, 5, 2, 6, 3, 7, 4]
myCommands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# 내 풀이 : 반복문 2개로 구현


def solution(arrary, commands):
    answer = []
    arraryS = []  # commands 배열에서 시작 인덱스만 추출해서 저장하기 위한 배열
    arraryE = []  # commands 배열에서 종료 인데스만 추출해서 저장하기 위한 배열
    arraryK = []  # commands 배열에서 k번째 값만 추출해서 저장하기 위한 배열

    for i in range(0, len(commands)):
        # 0 ~ commands(n-1)까지 반복하면서 start, end, k 인덱스 값 추출
        # zip함수를 이용해 commands[i]의 세개 값을 추출해서 따로 저장할 수 있음
        start, end, k = zip(commands[i])
        # 각각 추출한 값을 알맞은 배열에 list 형태로 추가
        # myCommands 배열의 start index 추가 결과 예시) [[2], [4], [1]]
        arraryS.append(list(start))
        arraryE.append(list(end))
        arraryK.append(list(k))
    # 0 ~ commands(n-1)까지 반복하면서 입력받은 arrary의 k번째 값을 추출해서, answer 배열에 저장
    for i in range(0, len(commands)):
        # start, end, k 번째 수에 맞는 배열에서 i번째 값 가져오기
        # 프로그래밍 방식의 인덱스 방식이 아니므로 start, k번째 값은 n-1을 하고, end값은 그대로 사용해서 대입
        start = arraryS[i][0] - 1
        end = arraryE[i][0]
        k = arraryK[i][0] - 1
        # arrary[start:end] 인덱스 값을 기준으로 임시 배열 생성
        temp = arrary[start:end]
        # sort() 함수를 이용해 오름차순으로 정렬
        temp.sort()
        # 정렬된 함수에서 k번째 인덱스값을 찾아서 answer 배열에 추가 후 리턴
        answer.append(temp[k])
    return answer


def solutionSimple(array, commands):  # 한줄로도 풀이 가능 (프로그래머스에서 찾은 정답)
    # 1) 람다 함수로 commands[0]번 인덱스값 -1 : commands[1]번 값을 추출하고, srot() 함수로 오름차순 정렬
    # 2) 정렬된 리스트내에서 k번(commands의 2번째 벨류-1)째 값을 대입하면서 람다 함수의 역할은 마무리
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    # 3) 람다함수의 인덱스별 계산 결과를 map함수로 감싸면 배열 전체를 돌면서 값을 생성함
    # 4) 리스트 형태로 답을 리턴해야하므로 list함수로 map함수 결과를 감싸면 마무리
