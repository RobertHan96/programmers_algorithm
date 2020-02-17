# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.


def solution(phone_book):
    phone_book.sort()  # 길이가 짧은 문자열부터 비교해야 outOfRange에러가 발생하지 않으므로, sort()를 먼저 적용
    for i in range(len(phone_book)-1):
        # 첫번째 인덱스 다음값을 첫번째 인덱스의 길이만큼 입력받아 같은지 비교
        if phone_book[0] == phone_book[i+1][:len(phone_book[0])]:
            return False
    return True


case1 = ['119', '97674223', '1195524421']
case3 = ['123', '456', '789']
print(solution(case3))
