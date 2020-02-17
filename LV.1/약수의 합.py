def solution(n):
    modifiers = []
    for i in range(1, n+1):
        if n % i == 0:
            modifiers.append(i)
    sum = 0
    for j in modifiers:
        sum = sum + j
    return sum


solution(5)
