## Q.61
#### 문제: https://programmers.co.kr/learn/courses/30/lessons/12951
#### 나의 풀이
``` 
def solution(s):
    split_s = s.split(' ')
    for i in range(len(split_s)):
        split_s[i] = split_s[i].capitalize()
    res = ' '.join(split_s)
    return res
```

- capitalizer라는 내장함수를 처음 알게 됐다.
- str의 첫 알파벳을 대문자화 해주는 기능이다.
- 첫 값이 알파벳이 아닌 숫자라면 pass