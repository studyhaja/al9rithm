### Q11. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12950
#### 문제:
<img width="689" alt="스크린샷 2021-02-07 오후 11 09 02" src="https://user-images.githubusercontent.com/70195733/107148990-8cea2500-6999-11eb-89d4-48ab0b9facc5.png">



#### my solution
```
def solution(arr1, arr2):
    answer = arr1
    for index1, i in enumerate(arr1):
        for index2, j in enumerate(i):
            answer[index1][index2] = arr1[index1][index2] + arr2[index1][index2]           
            
    return answer
```

#### 사고과정
1. return 값의 형태가 input 으로 주어지는 인자와 같으므로 처음에 똑같이 셋팅해준다.
2. 이중 리스트이므로 이중 포문을 돌면서, 같은 인덱스 값끼리 서로 더해준다.  이를 위해 enumerate 를 사용한다.

#### 다른 사람의 풀이
```
import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()

```
- 넘파이 들어만 봤고 사용하는건 처음봤다.
- 넘파이를 사용하니 문제가 간단히 해결되네?
- 넘파이 자체를 각잡고 공부할 것 까진 없고(아직까진), 이런식으로나마 조금씩 접해가보자.
