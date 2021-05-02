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
#### 문제: 음양더하기
<img width="690" alt="스크린샷 2021-04-27 오후 9 48 09" src="https://user-images.githubusercontent.com/70195733/116243793-463ee680-a7a2-11eb-9209-34365f7fd22d.png">

#### my solution
```
def solution(absolutes, signs):
    answer = 0
    for i in zip(absolutes, signs):
        if i[1]:
            answer += i[0]
        else:
            answer -= i[0]
    return answer
```
#### 사고과정
1. 요것도 쉬워서 사고과정은 pass
2. zip을 잘 쓰면 쉽게 끝난다.
3. 프로그래머스에서 푼 사람 횟수가 적으면 마냥 어려운 문제인 줄 알고 지레 겁부터 먹었었는데,<br>
꼭 그렇지만도 안더라. 비교적 최근에 올라온 문제는 난이도와 상관없이 당연히 푼 사람 횟수가 적다.
#### 다른 사람의 풀이

### Q 42. 
#### 문제: 폰켓몬
#### 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/1845
```
문제 설명
당신은 폰켓몬을 잡기 위한 오랜 여행 끝에, 홍 박사님의 연구실에 도착했습니다. 홍 박사님은 당신에게 자신의 연구실에 있는 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
홍 박사님 연구실의 폰켓몬은 종류에 따라 번호를 붙여 구분합니다. 따라서 같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다. 예를 들어 연구실에 총 4마리의 폰켓몬이 있고, 각 폰켓몬의 종류 번호가 [3번, 1번, 2번, 3번]이라면 이는 3번 폰켓몬 두 마리, 1번 폰켓몬 한 마리, 2번 폰켓몬 한 마리가 있음을 나타냅니다. 이때, 4마리의 폰켓몬 중 2마리를 고르는 방법은 다음과 같이 6가지가 있습니다.

첫 번째(3번), 두 번째(1번) 폰켓몬을 선택
첫 번째(3번), 세 번째(2번) 폰켓몬을 선택
첫 번째(3번), 네 번째(3번) 폰켓몬을 선택
두 번째(1번), 세 번째(2번) 폰켓몬을 선택
두 번째(1번), 네 번째(3번) 폰켓몬을 선택
세 번째(2번), 네 번째(3번) 폰켓몬을 선택
이때, 첫 번째(3번) 폰켓몬과 네 번째(3번) 폰켓몬을 선택하는 방법은 한 종류(3번 폰켓몬 두 마리)의 폰켓몬만 가질 수 있지만, 다른 방법들은 모두 두 종류의 폰켓몬을 가질 수 있습니다. 따라서 위 예시에서 가질 수 있는 폰켓몬 종류 수의 최댓값은 2가 됩니다.
당신은 최대한 다양한 종류의 폰켓몬을 가지길 원하기 때문에, 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택하려 합니다. N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.
가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.
입출력 예
nums	result
[3,1,2,3]	2
[3,3,3,2,2,4]	3
[3,3,3,2,2,2]	2
입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
6마리의 폰켓몬이 있으므로, 3마리의 폰켓몬을 골라야 합니다.
가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리, 2번 폰켓몬 한 마리, 4번 폰켓몬 한 마리를 고르면 되며, 따라서 3을 return 합니다.

입출력 예 #3
6마리의 폰켓몬이 있으므로, 3마리의 폰켓몬을 골라야 합니다.
가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리와 2번 폰켓몬 두 마리를 고르거나, 혹은 3번 폰켓몬 두 마리와 3번 폰켓몬 한 마리를 고르면 됩니다. 따라서 최대 고를 수 있는 폰켓몬 종류의 수는 2입니다.
```
#### my solution
```
def solution(nums):
    max_num = len(nums) // 2
    set_nums = set(nums)
    if len(set_nums) < max_num:
        return len(set_nums)
    return max_num
```
#### 사고과정
1. 중복값을 제거해야 하므로 set를 사용한다.
2. set의 길이가 1) N /2 보다 작거나, 2) N / 2 와 같거나 클 수 있다.
3. 1)의 경우는 set의 길이를 리턴, 2)면 N/2 길이를 리턴한다.
#### 다른 사람의 풀이

### Q 43. 
#### 문제: 실패율(프로그래머스)
#### 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42889
#### my solution
1차 시도(시간 초과로 실패)
```
def solution(N, stages):
    answer = {}
    # answer = []
    for i in range(1, N+1):
        challengers = 0
        failed = 0
        for j in stages:
            if j > i:
                challengers += 1
            elif j == i:
                challengers += 1
                failed += 1
        answer[i] = failed / challengers
        #answer.append((i, failed / challengers))
    answer = sorted(answer, reverse=True, key=lambda x: answer[x])
    return answer
```
2챠 시도(시간 초과 실패)
```
def solution(N, stages):
    answer = {}
    total_user = len(stages)
    for i in range(1, N + 1):
        challengers = total_user
        failed = stages.count(i)
        answer[i] = failed / challengers
        total_user -= failed
    answer = sorted(answer, reverse=True, key=lambda x: answer[x])
    return answer
```


3차 시도(성공)
```
def solution(N, stages):
    answer = {}
    total_user = len(stages)
    for i in range(1, N + 1):
        if total_user > 0:
            challengers = total_user
            failed = stages.count(i)
            answer[i] = failed / challengers
            total_user -= failed
        else:
            answer[i] = 0
            


    answer = sorted(answer, reverse=True, key=lambda x: answer[x])
    return answer
```
#### 사고과정
1. stage별로 파악해야 하므로 stage를 기준으로 for문을 돌린다.
2. 매 단계마다 전체 지원자 수를 줄여나간다.
3. 공식에 맞게 실패율을 구한다.
4. sorted안에 있는 key 람다를 통해 결과를 출력한다.

### Q 44. 
#### 문제:
#### my solution
```
```
#### 사고과정
#### 다른 사람의 풀이
