def solution(s):
    s_list = s.split(' ')
    s_list = list(map(int, s_list))
    s_list.sort()
    res = f"{s_list[0]} {s_list[-1]}"
    return res


s = "1 2 3 4"

print(solution(s))