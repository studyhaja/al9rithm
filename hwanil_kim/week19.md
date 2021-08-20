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
