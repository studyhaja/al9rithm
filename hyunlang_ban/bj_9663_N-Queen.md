## 문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

## 출력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

## 결과 - Fail
체스를 하나도 모름 + 그래프 공포증 ㅜㅜ

## Solution
```
def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)
```
진짜 신기한게, 복습할때 check 함수의 3번째 줄을 `row[i] == row[x]`로 바꿔서 썼는데 시간 초과로 테스트 통과를 못했다. 그래서 저 순서를 바꿔주니 시간 초과 문제가 해결되었다.. 도대체 무슨 차이일까? 🤔