### Q47.
#### 문제. https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
- 전화번호 목록

#### my_solution(첫시도)
- 다 통과했는데 효율성 테스트 4개중 2개에서 fail.
- 다른 사람의 풀이 보니 에전에는 이렇게 풀어도 통과됐는데, 요즘 효율성 기준이 빡빡해지면서 탈락하나보다.
```
def solution(phone_book):
    if len(phone_book) == 1:
        return False
    answer = True
    sorted_pbook = sorted(phone_book, key=len)
    for i in range(len(sorted_pbook)-1):
        for j in range(i+1, len(sorted_pbook)):
            if sorted_pbook[i] == sorted_pbook[j][:len(sorted_pbook[i])]:
                return False
    return answer
```

#### 다른 사람의 풀이
- 처음엔 앵? 어떻게 이게 되지 싶었는데 핵심은 sort였다.
- sort하면 1부터 차례로 정렬되고, 그래서 앞에거만 비교하면 된다고 한다.
- 아직 좀 의아함.
```
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

```