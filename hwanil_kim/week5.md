### Q22. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12947
#### 문제:
![스크린샷 2021-03-14 오후 9 35 02](https://user-images.githubusercontent.com/70195733/111068710-409c8280-850d-11eb-987a-4bfdb0175efb.png)

#### my solution
```
import math
def solution(n):
    res = 0
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            res += 1
    return res
```
#### 사고과정
1. 진작 풀긴 했는데, 효율성 테스트를 통 못해서 정말 애먹었다.
2. 에라토스테네스의 채로 푸는게 정석인 것 같은데 일단은 다른 방법으로 풀었다.
3. 예를 들어 100이 소수인지 판별하려면 100을 1부터 99까지 나눌 필요가 없다. 그러면 효율성 통과 못함.
4. 100의 약수는 100에 루트 쓰운 값을 중심에 두고 분포되어 있다.
5. 즉, 100의 약수는 100에 루트 씌운 값(10)보다 작은 값에 존재하고, 만약 이 범위에 약수가 없다면 이 수는 소수다.
6. 위 논리에 의해 문제를 풀면 된다. 2~ 어떤수의 루트씌운 값 까지만 검사하면 됨!


### Q23. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12915

#### 문제:
![스크린샷 2021-03-14 오후 10 08 06](https://user-images.githubusercontent.com/70195733/111069738-c6bac800-8511-11eb-975b-931d23a795c9.png)

#### my solution
```
def solution(strings, n):
    res = sorted(sorted(strings), key=lambda x: x[n])
    return res
```
#### 사고과정
1. 컨디션도 안좋고, 해법이 생각나지 않아서 구글링을 통해 풀었다.
2. 당연히 풀이를 먼저 이해하고, 해법을 적용했다.
3. sorted에 key를 사용할 수 있고, 여기에 lambda함수를 통해 특정 인덱스를 기준으로 소팅할 수 있다는 것을 처음 배웠다.
4. 순서가 같을 경우 사전순으로 배치하라고 했으므로, 정렬 전에 먼저 사전순으로 정렬해놓으면 된다.


### Q24. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3
#### 문제:
![스크린샷 2021-03-21 오전 12 00 19](https://user-images.githubusercontent.com/70195733/111874400-71caf600-89d8-11eb-8b45-d176cd5ea62d.png)

#### my solution
```
def solution(n, m):
    greatest_common_factor = 1
    least_common_multiple = n * m 
    for i in range(1, min(n,m) + 1):
        if n % i == 0 and m % i == 0:
            greatest_common_factor = i
    least_common_multiple = least_common_multiple / greatest_common_factor
    return [greatest_common_factor, least_common_multiple]
```
#### 사고과정
1. 두 수가 있다 했을 때 최대공약수는 두 수의 약수중 가장 큰 것이다.
-> 1~ 두 수중 작은 수 까지의 숫자로 두 숫자를 나눠서 0이 되는 것 중 가장 큰 값을 찾으면 된다.
2. 최소공배수는 두 수의 배수 중 가장 작은 값으로, 두 수를 곱한 뒤 최대공약수로 나누면 된다.
3. 유클리드 호제법으로 푸는게 제일 효율적인데 이건 나중에 해보기로 하고, 우선 위 논리에 의해서 풀었다.

