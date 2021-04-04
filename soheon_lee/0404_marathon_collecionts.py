def solution(participant, completion):
    counters = {}
    for p1 in participant:

        counters[p1] = counters.get(p1, 0) + 1

    for p2 in completion:
        counters[p2] -= 1

        if counters[p2] == 0:
            del counters[p2]

    return list(counters.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

# 다른 사람 풀이 가운데 신기했던 것 :
# collections 라는 모듈을 사용한 점.

