# 문제 설명
# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

# 제한사항
# a, b의 길이는 1 이상 1,000 이하입니다.
# a, b의 모든 수는 -1,000 이상 1,000 이하입니다.


a1 = [1,2,3,4]	
a2 = [-3,-1,0,2]


def solution(a, b):
    answer = 0
    for i in range(len(a)) : 
        answer += a[i] * b[i]
    return answer


# p = "00"
# s = "111111"

# p = "110"
# s = "110110110"

# p = "000"
# s = "00000000"

p = "101"
s = "10100010101101100" 


def est(p, s) : 
    answer = 0
    distance =  len(s) - len(p)

    if  s.find(p) != -1 : 
        for i in range(distance) :
            p += p[i]
        for i in range(len(s)) :
            if p[i] != s[i] : 
                answer += 1
    else : 
        answer = -1

    return answer

pins = ['960226-1019610', '960226-2319610'] 

test = list(map(lambda x: x.split("-")[1][0], pins))

print(test)