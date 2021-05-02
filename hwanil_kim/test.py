def solution(N, stages):
    answer = {}
    total_user = len(stages)
    for i in range(1, N + 1):
        challengers = total_user
        failed = stages.count(i)
        answer[i] = failed / challengers

    answer = sorted(answer, reverse=True, key=lambda x: answer[x])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))