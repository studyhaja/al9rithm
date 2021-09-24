def solution(s):
    split_s = s.split(' ')
    for i in range(len(split_s)):
        split_s[i] = split_s[i].capitalize()
    res = ' '.join(split_s)
    return res


s = "3people unFollowed me"

print(solution(s))