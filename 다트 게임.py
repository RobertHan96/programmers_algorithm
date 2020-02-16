def solution(dartResult):
    string = ''
    score = []
    for i in dartResult:
        if i.isnumeric() == True:
            string += i
        else:
            if i == "S":
                score.append(int(string)**1)
                string = ''
            elif i == "D":
                score.append(int(string)**2)
                string = ''
            elif i == "T":
                score.append(int(string)**3)
                string = ''
            elif i == "*":
                if len(score) > 1:
                    score[-2] = score[-2]*2
                score[-1] = score[-1]*2
            elif i == "#":
                score[-1] = score[-1]*-1
    return sum(score)


print(solution("1D2S#10S"))
