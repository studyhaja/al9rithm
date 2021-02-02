### Q1.

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12937

#### 문제:
<img width="707" alt="스크린샷 2021-02-02 오후 10 35 49" src="https://user-images.githubusercontent.com/70195733/106607887-25059a00-65a7-11eb-8978-d120cb1c529a.png">


#### my solution
```
def solution(num):
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



### Q3.

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12969

#### 문제:
<img width="690" alt="스크린샷 2021-02-02 오후 11 09 59" src="https://user-images.githubusercontent.com/70195733/106611860-ca227180-65ab-11eb-83af-21958b87825a.png">


#### my solution
```
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*" * a)
```

#### 사고과정
1. 총 b개의 줄이 생기므로 for문은 b로 돌린다.
2. 각 for문안에서 *을 a번만큼 프린트해준다.

#### 다른 사람의 풀이
```
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
```

비록 마지막 줄에도 \n이 생기긴 하지만, 이 문제를 for문 없이 접근할 생각 자체를 못하던 나에겐 신선한 충격을 준 코드다.



### Q4. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12948

#### 문제:
<img width="696" alt="스크린샷 2021-02-02 오후 11 21 30" src="https://user-images.githubusercontent.com/70195733/106613337-6b5df780-65ad-11eb-86c0-1f931a98baa6.png">


#### my solution
```
def solution(phone_number):
    return "*" * len(phone_number[:-4]) + phone_number[-4:]
```
#### 사고과정
1. 마지막 4자 기준으로 문자열을 슬라이싱 한다.
2. 4자 기준 앞문자열 수만큼 *을 써주고, 뒤 4자리와 합쳐준다.

### Q5. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12931

#### 문제:
<img width="667" alt="스크린샷 2021-02-02 오후 11 28 32" src="https://user-images.githubusercontent.com/70195733/106614207-63528780-65ae-11eb-9b2b-d4425832aa86.png">


#### my solution
```
def solution(n):
    n = str(n)
    res = 0
    for i in range(len(n)):
        res += int(n[i])

    return res
```

#### 사고과정
1. str 으로 만들어서 인덱싱을 사용할 수 있게 한다.
2. len만큼 for loop을 돌며 각각 자리수 값들을 더해 return한다.

#### 다른사람의 풀이
(1)
```
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 
```
이 사람은 재귀용법을 사용했다. 재귀를 배우긴 했지만 막상 문제풀 때 이를 활용해 풀 생각이 아직은 안난다.

(2)  
```
def sum_digit(number):
    return sum([int(i) for i in str(number)])
```
내가 푼 코드보다 짧고 가독성도 좋아 보인다. sum 내장 함수를 활용한 것도 훌륭한 듯.
