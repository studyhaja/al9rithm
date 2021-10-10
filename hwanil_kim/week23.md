## Q.62
#### 문제: https://www.acmicpc.net/problem/2675
#### 나의 풀이
``` 
case_num = int(input())
for i in range(case_num):
    res = ""
    cnt, chr = input().split()
    cnt = int(cnt)
    for c in chr:
        res += c * cnt
    print(res)
```
