# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때
# 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.


def isPrime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def solution(nums):  # 내가 짠 코드 별도의 isPrime 함수 생성
    count = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):  # 3중 for문으로 모든 경우의 수를 조합으로 가져옴
                n = (nums[i]+nums[j]+nums[k])
                if isPrime(n) == True:  # 소수 판별을 하고 True일때만 count 1증가
                    count += 1
    return count


case = [1, 2, 3, 4]
case2 = [1, 2, 7, 6, 4]


def cbSolution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):  # combinations 모듈을 통해 쉽게 가능한 모든 조합 생성 가능
        cand = sum(a)
        for j in range(2, cand):  # 1은 소수니까 제외하고, 2 ~ n까지 해당수를 나누면서 소수여부 판별
            if cand % j == 0:
                break  # 0이되면 소수가 아니므로 break로 넘어감
        else:  # 소수라면 answer 카운트 1증가
            answer += 1
    return answer
