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


### Q29.
### 문제: 하노이의 탑(재귀로 풀)

#### my solution
```
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg
        hanoi(num_disks - 1, start_peg, other_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, other_peg, end_peg)


# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)
```

#### 사고과정
1. base case: num_disks 가 0 이면 할 게 없으니 바로 return한다.
2. 탑을 지정된 위치로 옮기려면 제일 아래 있는 원반이 목적 기둥으로 가야하는데 그러게 위해선 제일 아래 원반을 제외한 원반은 다른 기둥(other_peg)으로 가야한다.
순서를 정리해보자.
1) 제일 아래 원반을 제외한 모든 원반을 other_peg로 옮긴다.
2) 제일 아래 원반을 목적 기둥으로 옮긴다.
3) 1)에서 옮겨놨던 원반들을 목적 기둥으로 옮긴다.

### Q 30.
### 문제: 가까운 매장 찾기
![](https://images.velog.io/images/kpl5672/post/1bd6c248-07f0-4f1f-adaa-c5157c6d07e4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-11%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%208.06.11.png)
![](https://images.velog.io/images/kpl5672/post/52635ddc-8d3f-4814-ba1e-513c07e175a6/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-11%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%208.06.15.png)

#### my solution
```
# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    temporary = {}
    for index in range(len(coordinates)):
        for index2 in range(index+1, len(coordinates)):
            res = distance(coordinates[index], coordinates[index2])
            temporary[res] = [coordinates[index], coordinates[index2]]
    shortest = min(temporary.keys())
    return temporary[shortest]
            
```

#### 사고과정 및 반성
1. 인덱스를 이용해 이중 포문을 돌면서 값을 서로 비교하면 된다.
2. 나는 딕셔너리를 만들고 모든 값을 저장한 반, 정답풀이는 초기값만 지정해놓고 특정 조건에 맞으면 초기값만 오버라이드 해주는 방법을 썼다. 이게 더 좋아보인다. 하나 배웠다.
3. 나는 첫 포문을 len(coordinates)로 해줬는데 사실 len(coordinates) -1 로 했어야 한다. 이렇게 안해도 정답은 맞긴 맞았지만 엄격한 채점 시스템에 오답이었을 것이다.

#### 다른 사람의 풀이
```
# 제곱근 사용을 위한 sqrt 함수 불러오기
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 현재까지 본 가장 가까운 두 매장
    pair = [coordinates[0], coordinates[1]]
  
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]

            # 더 가까운 두 매장을 찾으면 pair 업데이트
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]

    return pair
```


### Q 31.
#### 문제: 강남역 폭우
![](https://images.velog.io/images/kpl5672/post/dcd75d00-6d74-4ba1-ac69-73f143f4faa0/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-11%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.14.18.png)
#### my solution
```
def trapping_rain(buildings):
    answer = 0
    for index in range(len(buildings)):
        if index == 0 or index == len(buildings) - 1:
            continue
        else:
            left_max = max(buildings[:index])
            right_max = max(buildings[index+1:])
            capacity = min(left_max, right_max) - buildings[index]
            if capacity > 0:
                answer += capacity
    return answer
```
#### 사고과정
- 일단 가장자리(맨 왼쪽, 맨 오른쪽)인덱스에는 물을 받을 수 없다.
- 그외 인덱스들의 경우, 왼쪽 중 가장 큰것과 오른쪽 중 가장 큰것 중 작은 것보다 작다면 물을 받을 수 있다.
- 위 연산을 해서 값이 +일경우만 물을 받을 수 있고, 아니라면 패스한다.


