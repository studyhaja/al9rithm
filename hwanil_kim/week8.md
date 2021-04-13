### Q 34.
#### 문제: 최소 동전으로 거슬러 주기
```
최소 동전으로 돈을 거슬러 주는 함수를 Greedy Algorithm으로 구현해 보겠습니다.

우리가 작성할 함수 min_coin_count는 거슬러 줘야 하는 총액 value와 동전 리스트 coin_list를 파라미터로 받고, 거슬러 주기 위해 필요한 최소 동전 개수를 리턴합니다.

예를 들어 1170원을 거슬러 주기 위해서는 500원 2개, 100원 1개, 50원 1개, 10원 2개를 줄 수 있기 때문에 6을 리턴하면 되겠죠?

동전의 조합은 항상 500원, 100원, 50원, 10원이라고 가정합시다.
```
#### my solution
```
def min_coin_count(value, coin_list):
    res = 0
    value1 = 0
    coin_list.sort(reverse=True)
    for coin in default_coin_list:
        coin_num = value // coin
        res += coin_num
        value -= coin_num * coin
        if value == 0:
            return res
        
    # 코드를 작성하세요.

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
```
#### 사고과정
#### 다른 사람의 풀이
```
def min_coin_count(value, coin_list):
    # 누적 동전 개수
    count = 0

    # coin_list의 값들을 큰 순서대로 본다
    for coin in sorted(coin_list, reverse=True):
        # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인한다
        count += (value // coin)

        # 잔액을 계산한다
        value %= coin

    return count
```

### Q 35.
#### 문제:
#### my solution
#### 사고과정

### Q 36.
#### 문제:
#### my solution
#### 사고과정

### Q 37.
#### 문제:
#### my solution
#### 사고과정

### Q 38.
#### 문제:
#### my solution
#### 사고과정
