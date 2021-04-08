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

