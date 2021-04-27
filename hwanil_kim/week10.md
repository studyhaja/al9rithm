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


### Q 39. 
#### 문제: 소수 만들기
<img width="697" alt="스크린샷 2021-04-27 오후 4 47 15" src="https://user-images.githubusercontent.com/70195733/116205021-4b873b80-a778-11eb-83e2-a4a3b42a0b46.png">

#### my solution
```
def solution(nums):
    answer = 0
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                three_sum = nums[i] + nums[j] + nums[k]
                if is_prime(three_sum):
                    answer += 1
    return answer


import math
def is_prime(num):
    """소수 여부 판별하는 함수"""
    res = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            res += 1
    if res > 1:
        return False
    return True
```
#### 사고과정
1. 숫자 3개를 비교하므로 3중 for문을 돌린다.
2. 이때 포인트는 숫자가 중복되지 않게 i, i+1, i+2의 형태로 인덱스를 주는 것이다.
3. 소수 판별하는 함수를 따로 빼서 쓰자.
4. 소수 판별은 sqrt를 사용해서 시간복잡도를 줄인다!

#### 다른 사람의 풀이
```
class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def solution(a):
    answer = ALWAYS_CORRECT()
    return answer;
```
1. 문제 자체를 해킹(?)해서 항상 정답이 되도록 하는 요상한 방법을 쓴 사람이 있다.
2. 당연히 출제자가 원하는 답은 아니지만 이런걸 할 생각을 했다는 것 자체가 대단하다ㅋㅋ.
3. 덕분에 `__eq__`에 대해 공부하게 됐다. 
4. 이런게 바로 모든 일을 통해 배우고 교훈을 얻는 태도인가ㄷㄷ

```
from itertools import combinations as cb
import math


def solution(nums):
    answer = 0
    for i in cb(nums, 3):
        three_sum = sum(i)
        if is_prime(three_sum):
            answer += 1
    return answer



def is_prime(num):
    """소수 여부 판별하는 함수"""
    res = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            res += 1
    if res > 1:
        return False
    return True
```
- 내장된 combinations라는 게 있는지 처음 알았다.
 3중 포문 돌릴 필요 없이 combinations쓰면 엄청 간단해지겠다 싶어서 적용해서 풀어봤다.
### Q 40. 
#### 문제: 내적
<img width="703" alt="스크린샷 2021-04-27 오후 9 27 09" src="https://user-images.githubusercontent.com/70195733/116241126-8781c700-a79f-11eb-8cd6-fd25b1cc92ea.png">

#### my solution
1번 풀이
```
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer
```

2번 풀이
```
def solution(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])
```
#### 사고과정
1. 쉬워서 굳이 사고과정은 안적어도 될 것 같다.
2. 두 개의 풀이 중 뭐가 더 좋은걸까? 2번이 짧고 간지나긴 한다만, 가독성 측면에서는 1번이 낫다고 보인다.
3. 실제 시험을 본다면 어떤 식으로 푸는게 좋을라나.

### Q 41. 
#### 문제:
#### my solution
```
```
#### 사고과정
#### 다른 사람의 풀이

### Q 42. 
#### 문제:
#### my solution
```
```
#### 사고과정
#### 다른 사람의 풀이
