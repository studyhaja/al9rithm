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



### Q6. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12944

#### 문제:
<img width="575" alt="스크린샷 2021-02-03 오후 9 36 37" src="https://user-images.githubusercontent.com/70195733/106748086-103d0b00-6668-11eb-80eb-2d5e882c610d.png">


#### my solution
```
def solution(arr):
    return sum(arr) / len(arr)
```

#### 사고과정
1. 평균은 전체 합 나누기 전체 개수다.
2. 전체 합은 리스트에 sum을 씌워 구하고, 전체 개수는 리스트에 len을 씌워 구한다.



### Q7. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12926

#### 문제:
<img width="700" alt="스크린샷 2021-02-03 오후 9 55 11" src="https://user-images.githubusercontent.com/70195733/106749977-92c6ca00-666a-11eb-9623-f5de74f01ac3.png">


#### my solution
```
def solution(s, n):
    answer =""
    for i in s:
        ascii_num = ord(i)
        if ascii_num == 32:
            answer += ""
        elif ascii_num in range(65, 91):
            ascii_num += n
            if ascii_num > 90:
                ascii_num = ascii_num - 90 + 64
        elif ascii_num in range(97, 123):
            ascii_num += n
            if ascii_num > 122:
                ascii_num = ascii_num - 122 + 96
        answer += chr(ascii_num)
    return answer
```

#### 사고과정
1. 알파벳을 특정 숫자만큼 밀기 위해선 순서가 필요한데, 이를 위해 알파벳과 알파벳을 이어주는 ord, chr내장함수를 사용하자.
2. 공백은 그대로 유지하면 되는 규칙을 기억하자.
3. 밀린 알파벳이 z, 혹은 Z를 넘어가면 소문자는 a, 대문자는 A부터 다시 시작해야 하므로, 소문자와 대문자를 나눠서 처리한다.

#### 다른 사람의 풀이
- 대/소문자를 구별하기 위해,
1) isupper(), islower()함수를 사용하거나
2)  i >= 'A' and i <= 'Z' <br>
이런 식으로 표현한 사람들의 코드가 인상적이었다.


### Q8. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12930

#### 문제:
<img width="689" alt="스크린샷 2021-02-03 오후 10 13 51" src="https://user-images.githubusercontent.com/70195733/106751910-33b68480-666d-11eb-8b1f-87697ed4558b.png">


#### my solution
```
def solution(s):
    s = s.split(' ')
    answer = []
    for word in s:
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        answer.append(new_word)
    return ' '.join(answer)
```

#### 사고과정
1. 공백 기준으로 단어를 나눠야 하므로 split을 사용한다.
2. for loop으로 각 단어에 하나씩 접근한다.
3. 각 단어의 인덱스를 알기 위해 len()으로 다시 for을 돌며, 짝수일 땐 대문자화, 홀수일 떈 소문자화 한다.


### Q9. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12932

#### 문제:
<img width="691" alt="스크린샷 2021-02-03 오후 10 35 09" src="https://user-images.githubusercontent.com/60768642/106754366-3c5c8a00-6670-11eb-95c5-2bdb06761bf2.png">


#### my solution
```
def solution(n):
    n = list(str(n))
    res = []
    while len(n) != 0:
        res.append(int(n.pop()))
    return res
```

#### 사고과정
1. 가공하기 쉽게 str화 한다.
2. 뒤에서부터 하나씩 꺼내서(pop) 새로운 list에 append한다. 

#### 다른 사람의 풀이
```
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
```
내장함수로 간단하게 해결할 수 있는걸, 그게 생각이 안나면 돌고 돌아 풀게 된다.
이번 문제가 그런 경우였다.
하지만 초보때는 너무 내장함수에 의지하지 말고, 오히려 직접 그 기능을 구현해보는 것도
좋은 방법이라고 어디서 들었다. 그런 말로 위안 삼으며 정신승리를 해본다.
(그치만 다음에 다시 뭔가를 뒤집는 문제를 만나게 된다면  reverse와 reversed를 먼저 떠올려보자..)



### Q10. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12934

#### 문제:
<img width="700" alt="스크린샷 2021-02-04 오후 9 43 51" src="https://user-images.githubusercontent.com/60768642/106894302-1d263100-6732-11eb-837e-f5c4f22877ce.png">


#### my solution
```
import math

def solution(n):
    sqrt_n = math.sqrt(n)
    if sqrt_n == int(sqrt_n):
        return (sqrt_n + 1) ** 2
    return -1
```

#### 사고과정
1. sqrt로 제곱근을 구할 수 있다.
2. 정수 제곱근은 2.0과 같은 숫자가 나오고, 그렇지 않으면 2.12312412같은 식으로 나온다.
3. 2를 근거로, sqrt를 씌운 것 == int(sqrt)의 결과가 같다는 정수 제곱근으로 판별한다.

#### 다른 사람의 풀이
```
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
```
- `n ** (1/2)`으로 n의 제곱근을 구한 점이 기똥차다.
- `n % 1 ==0` 으로 정수여부를 판단해낸 점이 기똥차다.
- 한수 배웠다.



