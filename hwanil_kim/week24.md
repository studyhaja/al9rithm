## Q.63
#### 문제: 지불해야 하는 값이 4720원 일 때 1원 50원 100원, 500원 동전으로 동전의 수가 가장 적게 지불하기.
#### 전략
- 가장 큰 동전부터 최대한 지불하는 방식으로 구현 가능
- 탐욕 알고리즘으로 매 순간 최적이라 생각되는 경우를 선택하면 됨.
#### 나의 풀이
``` 
def get_minimum_coin():
    coin_list = [1, 50, 100, 500]
    amount = 4720
    coin_num = 0

    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_num += amount // coin
        amount = amount % coin
        if amount == 0:
            return coin_num
```
