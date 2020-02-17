
# 같은수를 체크하는게 중요 set 함수 활용하여 쉽게 해결가능 ex) set()한 길이가 1이면 4개의 눈이 다 같다는 의미
# N = int(input("주사위를 굴린 사람 수 입력 : "))
# score_input = sorted(list(map(int, input("주사위 눈 결과 입력 : ").split())))
# score = [i for i in score_input]

TC1 = [[3, 3, 3, 3], [3, 3, 6, 3], [2, 2, 6, 6], [6, 2, 1, 5]]
# 65000, 13000, 6000, 600 원이 나와야함


def solution(N, scores):
    answer = []
    for i in scores:
        if len(set(i)) == 1:
            answer.append(50000+i[0]*5000)
            print(f"모든 눈이 맞을때 : {50000+i[0]*5000}")
        elif i[0] == i[1] and i[2] == i[3]:
            answer.append(2000+i[0]*500+i[-1]*500)
            print(f"2쌍이 맞을떄 : {2000+i[0]*500+i[-1]*500}")
        elif len(set(i)) == 4:
            answer.append(max(i)*100)
            print(f"모든 눈이 다를때 : {max(i)*100}")
        else:
            if i[0] == i[1] or i[0] == i[2] or i[0] == i[3]:
                answer.append(10000+i[0]*1000)
                print(f"3쌍이 맞을때 {10000+i[0]*1000}")
            else:
                answer.append(10000+i[1]*1000)
                print(f"3쌍이 맞을때 {10000+i[1]*1000}")

    return max(answer)


print(solution(5, TC1))
