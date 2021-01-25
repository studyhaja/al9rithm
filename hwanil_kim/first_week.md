### Q1.

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12917

#### 문제:
<img width="703" alt="스크린샷 2021-01-25 오후 12 18 01" src="https://user-images.githubusercontent.com/60768642/105668138-11f82780-5f20-11eb-8ff7-0bc19d216cb8.png">


#### my solution
```
def solution(s):
    return ''.join(sorted(s, reverse=True))
```

#### 사고과정
1. 알파벳을 역정렬 하기 위해서 sorted()함수를 사용한다.
2. sorted함수는 A-Z a-z순으로 정렬이 되는데, 문제에선 역순을 요구했기 때문에 \n
reverse=True 옵션을 주어서 역정렬 시킨다.
3. sorted()함수의 결과값은 리스트이기 떄문에 ''.join()을 사용해서 str화한다.


### Q2.

#### Q_link : "https://programmers.co.kr/learn/courses/30/lessons/12910"

#### 문제
<img width="703" alt="스크린샷 2021-01-25 오후 12 18 01" src="https://user-images.githubusercontent.com/60768642/105709991-d7ab7c00-5f59-11eb-97dc-397b5657aafc.png">


#### my solution
```
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return sorted(answer)
```

#### 사고과정:
1. 나누어 떨어지는지 여부는 %를 사용하여 판별한다. ( a % b ==0이면 a는 b로 나누어떨어짐)
2. 오름차순 정렬을 위해 sorted() 혹은 sort를 활용한다.

#### solution of others

```
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
```
