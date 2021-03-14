strings = ["sunn", "beddd", "carrrr"]
n = 1

def solution(strings, n):
    res = sorted(strings, key=lambda x: x[1])
    return res

a = solution(strings, n)
print(a)