### Q26. 
#### 문제링크: 
#### 문제:
재귀 삼각함수(코드잇 문제)
![](https://images.velog.io/images/kpl5672/post/20ca2d92-8a21-4eec-8a85-0b1ce392f3c3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.00.48.png)
#### my solution
```
def triangle_number(n):
    if n == 1:
        return 1
    else:
        return n + triangle_number(n-1)
```
#### 사고과정
재귀적 문제에서는 recursive case와 base case 두 가지로 나눌 수 있다.
Recursive case: 현 문제가 너무 커서, 같은 형태의 더 작은 부분 문제를 재귀적으로 푸는 경우
Base case: 이미 문제가 충분히 작아서, 더 작은 부분 문제로 나누지 않고도 바로 답을 알 수 있는 경우

먼저 base case에 대한 생각을 하고, recursive를 생각하면 편하다.
base case는 n이 1이면 return 1을 하는 것이다.
그 외에 n이 주어졌을 땐 triangle_number(n-1)값과 n을 더하면 된다.


### Q27. 
#### 문제링크: 
#### 문제:
자릿수의 합 재귀(코드잇 문제)
![](https://images.velog.io/images/kpl5672/post/20ca2d92-8a21-4eec-8a85-0b1ce392f3c3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.00.48.png)
#### my solution
```
def sum_digits(n):
    if n < 10:
        return n
    else:
        return int(str(n)[-1]) + sum_digits(int(str(n)[:-1]))
```
#### 사고과정
- base case: n의 길이가 1이면, 혹은 n이 10보다 작으면 return n
- recursive case: n의 길이가 2보다 크면, 맨 마지막 수 + sum_digits(n-1)을 한다.

### Q28. 
#### 문제링크: 
#### 문제:
![](https://images.velog.io/images/kpl5672/post/3e1042f2-c661-4b09-923e-85da719a2dd9/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.41.58.png)
#### my solution
```
def flip(some_list):
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
    else:
        return some_list[-1:] + flip(some_list[:-1])
```
#### 사고과정
-base case: some_list의 len이 0 혹은 1이면 some_list를 리턴한다.
- revursive case: [-1:]와 some_list([:-1])을 더해준다.

시간 복잡도:  O(n^2)
