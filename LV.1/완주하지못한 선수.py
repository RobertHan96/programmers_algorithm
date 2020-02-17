def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return participant[0]


a = ["mislav", "stanko", "mislav", "ana"]
b = ["stanko", "mislav", "ana"]

solution(a, b)
