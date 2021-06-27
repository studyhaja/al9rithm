### Q46.
#### 문제.
- 링크: https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3


#### my_solution
```
def get_divisor_count(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt
        

def solution(left, right):
    total = 0
    for i in range(left, right+1):
        divisor_count = get_divisor_count(i)
        if divisor_count % 2 == 0:
            total += i
        else:
            total -= i
    return total
```

#### 다른 사람의 풀이
제곱근이 있는 수는 약수가 홀수개 라는 것을 이용해서 문제를 쉽게 푼 사람이 있었다.
- 2이면 1, 2 -> 2개
- 3이면 1, 3 -> 2개
- 4이면 1, 2, 4 -> ***3개***
- 5이면 1, 5 -> 2개
- 6이면 1, 2, 3, 6 -> 4개
- 7이면 1, 7 -> 2개
- 8이면 1, 2, 4, 8 -> 4개
- 9이면 1, 3, 9 -> ***3개***
- 10이면 1, 2, 5, 10 -> 4개
- 11이면 1, 11 -> 2개
- 12이면 1, 2, 3, 4, 6, 12 -> 6개

```
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
```

