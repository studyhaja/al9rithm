def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if is_prime(i):
            answer += 1
    return answer


def is_prime(num):
    if num == 2:
        return True
    for j in range(2, num):
        if num % j == 0:
            return False
    return True

solution(10)