### Q19. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/42862
#### 문제:
<img width="707" alt="스크린샷 2021-02-16 오후 11 13 24" src="https://user-images.githubusercontent.com/70195733/108074577-b814f880-70ac-11eb-9789-ad3da96ee8fb.png">
<img width="691" alt="스크린샷 2021-02-16 오후 11 13 29" src="https://user-images.githubusercontent.com/70195733/108074580-b9debc00-70ac-11eb-98c2-feb29f79afb3.png">

#### my solution
```
def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    for i in new_reserve:
        if i - 1 in new_lost:
            new_lost.remove(i - 1)
            continue
        elif i + 1 in new_lost:
            new_lost.remove(i + 1)
            continue
    answer = n - len(new_lost) 
    return answer

```
#### 사고과정
1. 잃어 버린 사람이 여분을 가져온거는 없다 치면 되니까 제거해준다.
2. 여분 리스트로 for loop을 돌며 lost에 현재 값 보다 하나 작은 수와 큰 수가 있는지 확인하고 있다면 제거한다.
3. n 에서 lost의 크기만큼 빼면 구하고자 하는 값이 나온다.

### Q20. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12947
#### 문제:
#### my solution
#### 사고과정

### Q21. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12947
#### 문제:
#### my solution
#### 사고과정
