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


### Q3.

#### Q link: https://programmers.co.kr/learn/courses/30/lessons/12906

#### 문제
<img width="703" alt="스크린샷 2021-01-28 오후 11 00 48" src="https://user-images.githubusercontent.com/60768642/106148692-b4ccd200-61bc-11eb-943d-8c5cf7e0bfd8.png">


#### my solution
```
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            continue
        answer.append(arr[i])
    return answer
```

#### 사고과정
1. 빈 리스트를 만들고 결과값들을 append하는 전략을 쓴다(순차적으로 값을 만들어 return해야 하기 때문에)
2. 인덱스 0번은 무조건 append한다.
3. 인덱스 1번부터, 직전 인덱스 숫자와 비교하여 같으면 pass하고, 다르면 append한다.


#### 다른 사람의 풀이
```
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
```

### Q4.

#### Q link: https://programmers.co.kr/learn/courses/30/lessons/42840
#### 문제
<img width="665" alt="스크린샷 2021-01-29 오후 10 22 49" src="https://user-images.githubusercontent.com/60768642/106279971-9f20e080-6280-11eb-80ab-d17fe27bef60.png">
#### my solution

```
def solution(answers):
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == n1[i % 5]:
            cnt1 += 1
        if answers[i] == n2[i % 8]:
            cnt2 += 1
        if answers[i] == n3[i % 10]:
            cnt3 += 1
    max_cnt = max(cnt1, cnt2, cnt3)
    if cnt1 == max_cnt:
        answer.append(1)
    if cnt2 == max_cnt:
        answer.append(2)
    if cnt3 == max_cnt:
        answer.append(3)
    return answer
```

####사고과정
1. 일단 정해진 패턴 3개를 담은 리스트를 만든다.
2. input받은 값의 len으로 for loop을 돌며 인덱스를 통해 input과 패턴 3개의 값을 비교해서 같을 경우 포인트를 1씩 증가시켜준다.
3. for loop이 끝나고 제일 큰 값을 찾는다.
4. 제일 큰 값이 2개 이상일 수도 있으니 하나씩 확인해가며 제일 큰 값을 순서대로 결과 리스트에 추가해준다.



### Q5.
####문제: 회문(palindrome) 만들기

회문설명 :
- 원 단어를 거꾸로 뒤집어도 똑같은 단어
- 'level'은 회문이다.
- 'top'은 회문이다.
- 1 글자일 경우 return True한다.

#### 풀이 1. for문 활용
```
def check_palindrome(data):
    res = True
    for i in range(len(data)):
        if data[i] == data[-(i+1)]:
            pass
        else:
            res = False
    return res

```

#### 풀이 2. 재귀용법 활용
```
def check_palindrome(data):
    if len(data) == 1:
        return True
    if data[0] == data[-1]:
        return check_palindrome(data[1:-1])
    return False

```


### Q6.
####문제: 
<img width="576" alt="스크린샷 2021-01-31 오후 12 29 34" src="https://user-images.githubusercontent.com/60768642/106373816-bbc43200-63c0-11eb-9903-461477833664.png">


#### 풀이(재귀용법 활용):
```
def until_one(num):
    print(num)
    if num == 1:
        return num
    
    if num % 2 == 0:
        #짝수
        return until_one(int(num / 2))
    else:
        #홀수
        return until_one((3 * num) + 1)

a = until_one(20)
print(a)
```

### Q7.
#### 문제:
<img width="682" alt="스크린샷 2021-01-31 오후 12 31 08" src="https://user-images.githubusercontent.com/60768642/106373831-d3031f80-63c0-11eb-864b-5e9651b4a0cf.png">

#### 풀이(재귀용법):
```
def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    return func(data-1) + func(data-2) + func(data-3)
```
