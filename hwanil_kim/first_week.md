#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12917

#### 문제:
<img width="703" alt="스크린샷 2021-01-25 오후 12 18 01" src="https://user-images.githubusercontent.com/60768642/105668138-11f82780-5f20-11eb-8ff7-0bc19d216cb8.png">


#### my solution
```
def solution(s):
    return ''.join(sorted(s, reverse=True))
```

#### 사고과정
1. 알파벳을 역정렬 하기 위해서 sorted()함수를 사용한다.
2. sorted함수는 A-Z a-z순으로 정렬이 되는데, 문제에선 역순을 요구했기 때문에 \n
reverse=True 옵션을 주어서 역정렬 시킨다.
3. sorted()함수의 결과값은 리스트이기 떄문에 ''.join()을 사용해서 str화한다.


