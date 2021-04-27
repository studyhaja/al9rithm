### Q 37.
#### 문제: 2016년(프로그래머스)
<img width="702" alt="스크린샷 2021-04-26 오후 10 59 58" src="https://user-images.githubusercontent.com/70195733/116095217-2e545d80-a6e3-11eb-94be-26320406007b.png">

#### my solution
```
def solution(a, b):
    from datetime import datetime
    day = datetime(2016, a, b).weekday()
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    answer = days[day]
    return answer
```
#### 사고과정
1. 쉽게 풀기 위해 datetime모듈을 사용한다.
2. datetime의 weekday()는 월요일~일요일을 0~6숫자로 리턴해준다.

### Q 38. 
#### 문제: 예산(프로그래머스)
<img width="690" alt="스크린샷 2021-04-27 오후 3 57 34" src="https://user-images.githubusercontent.com/70195733/116198843-6b673100-a771-11eb-9997-39b7e27d6e96.png">
<img width="689" alt="스크린샷 2021-04-27 오후 3 57 39" src="https://user-images.githubusercontent.com/70195733/116198851-6e622180-a771-11eb-9f11-b1d0787c69c9.png">

#### my solution
```
def solution(d, budget):
    res = 0
    answer = 0
    for num in sorted(d):
        if res + num <= budget:
            res += num
            answer += 1
    return answer
```
#### 사고과정
1. d를 오름차순으로 정렬한 후 budget을 넘지 않는 선에서 차례로 더해가면 된다!
#### 다른 사람의 풀이
```
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
```

1. 역으로 큰 것부터 하나씩 빼가면서 연산할 생각을 했다는 게 참신했다.