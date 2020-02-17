# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다.
# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.

# 입출력 예
# a = 5, b= 24 => 'THU'

# 입력된 날짜의 요일 계산을 위해 datetime 모듈 임포트
import datetime


def solution(a, b):
    answer = ''
    # 주어진 문제와 같이 요일을 순서대로 정의한 리스트 생성
    weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    # 연도는 2016년으로 고정이므로 값을 넣고, 월/일은 a/b 값을 대입하고 weekday() 함수를 이용해 요일의 인덱스 값을 구함
    # ex) 월요일 = 0, 일요일 = 6
    date = datetime.datetime(2016, a, b).weekday()
    # weekdays리스트를 돌면서 i값과 date의 값을 비교해서 같다면 결과를 리턴함
    for i in range(0, len(weekdays)):
        if i == date:
            # 문제는 일요일이 0번째 인덱스이므로 값을 초과해서 구할수 없으므로, 이 경우 강제로 weekdays 배열의 0번째 값을 할당
            if date == 6:
                answer = weekdays[0]
            else:
                # datetime 모듈과 달리 문제는 일요일이 첫번째 값이므로 i+1을해서 결과로 저장
                answer = weekdays[i+1]
    return answer


print(solution(1, 3))
