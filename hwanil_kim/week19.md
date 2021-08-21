## Q.54

#### 문제. https://www.acmicpc.net/problem/1966 (프린터 큐)
#### 나의 풀이
```
number_of_case = int(input())

answer = []

for _ in range(number_of_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    greatest = max(queue)
    queue = [(i, idx) for idx, i in enumerate(queue)]

    cnt = 0
    while True:
        pop_data = queue.pop(0)
        if pop_data[0] == greatest:
            cnt += 1
            if pop_data[1] == m:
                answer.append(cnt)
                break
            greatest = max(queue, key=lambda x: x[0])[0]
        else:
            queue.append(pop_data)
print(*answer, sep='\n')

```

## Q.55
#### 문제:https://www.acmicpc.net/problem/5397 (키로거)
#### 나의 풀이
- 결국 강의 보고 풀었다.
- 핵심은 커서동작을 코드에 반영하는 것이다.
- 이를 위해 스택 두개를 쓰고 그 가운데에 커서를 두는 개념을 사용했다.
``` 
number_of_case = int(input())
for i in range(number_of_case):
    l_stack = []
    r_stack = []
    case = input()
    for chr in case:
        if chr == '<':
            if l_stack:
                poped_data = l_stack.pop()
                r_stack.append(poped_data)
        elif chr == '>':
            if r_stack:
                poped_data = r_stack.pop()
                l_stack.append(poped_data)
        elif chr == '-':
            if l_stack:
                l_stack.pop()
        else:
            l_stack.append(chr)
    l_stack.extend(reversed(r_stack))
    print(''.join(l_stack))
```