## Q.53 스택수열

#### 문제. https://www.acmicpc.net/problem/1874
#### 나의 풀이
```
n = int(input())
cnt = 1
stack = []
res = []

for i in range(n):
    data = int(input())
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        res.append('+')
    if stack[-1] == data:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        exit(0)
print('\n'.join(res))

```
