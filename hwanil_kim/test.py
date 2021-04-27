def solution(absolutes, signs):
    answer = 0
    for i in zip(absolutes, signs):
        if i[1] == "true":
            answer += i[0]
        else:
            answer -= i[0]
    return answer


a = [4,7,12]
b = ["true","false","true"]

c = solution(a, b)
print(c)

