def solution(n, m):
    greatest_common_factor = 1
    least_common_multiple = n * m
    print(least_common_multiple)
    for i in range(1, min(n,m) + 1):
        if n % i == 0 and m % i == 0:
            greatest_common_factor = i
    least_common_multiple = least_common_multiple / greatest_common_factor
    return [greatest_common_factor, least_common_multiple]

a = solution(2, 5)
print(a)