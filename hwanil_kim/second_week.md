### Q1.

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12937

#### 문제:
<img width="707" alt="스크린샷 2021-02-02 오후 10 35 49" src="https://user-images.githubusercontent.com/70195733/106607887-25059a00-65a7-11eb-8978-d120cb1c529a.png">


#### my solution
```
`def solution(num):
    return "Even" if num % 2 == 0 else "Odd"
```

#### 사고과정
1. 홀수, 짝수여부는 2로 나눴을 때 나머지가 0인지 아닌지로 판별한다.



### Q2.

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12928
#### 문제:
<img width="594" alt="스크린샷 2021-02-02 오후 10 56 57" src="https://user-images.githubusercontent.com/70195733/106610319-fa691080-65a9-11eb-9c01-4560e9a4d14c.png">


#### my solution
```
`def solution(n):
    res = 0
    for i in range(1, n):
        if n % i == 0:
            res += i
    res += n
    return res
```

#### 사고과정
1. 1부터 n까지 for문을 돌린다.
2. n을 for loop에서 나온 숫자와 %연산을 한 값이  0이면 나눠진다는 뜻이니 이 숫자들을 더해서 return한다.

#### 다른 사람의 풀이
```
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
```

n 값의 절반 이상부터는 검사할 필요 없다는 점을 활용해서 코드 성능을 더욱 향상시켰다.
