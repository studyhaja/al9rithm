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



### Q12. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12954
#### 문제:
<img width="705" alt="스크린샷 2021-02-08 오후 11 15 57" src="https://user-images.githubusercontent.com/70195733/107231427-a5267680-6a63-11eb-8fc1-411135c11540.png">




#### my solution
```
def solution(x, n):
    return [x * i for i in range(1, n+1)]
```

#### 사고과정
1. 결과값은 x와 1~n을 차례대로 곱한 값들을 모은 list다.
2. 이를 list comprehension으로 간단하게 구현 가능할 것 같다.


### Q13. 

#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12947
#### 문제:
<img width="712" alt="스크린샷 2021-02-08 오후 11 34 06" src="https://user-images.githubusercontent.com/70195733/107233710-35fe5180-6a66-11eb-8806-3255d4810710.png">





#### my solution
```
def solution(x):
    if x % sum([int(i) for i in str(x)]) == 0:
        return True
    return False
```

#### 사고과정
1. 자릿수 합은 숫자를 str으로 만들어 for loop을 돌며 하나씩 꺼내고, 꺼낸 값을 int로 만들어 더하면 된다.
2. 나눈 나머지가 0이면 나누어 떨어지는 것이고, 그렇지 않다면 아니다.


### Q14. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3#
#### 문제:
![스크린샷 2021-02-12 오후 11 20 37](https://user-images.githubusercontent.com/60768642/107779634-006ca780-6d89-11eb-8c27-8c97ae6a02d5.png)

#### my solution
```
def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr

```
#### 사고과정
1. 길이가 1이면 무조건 [-1]을 리턴한다.
2. min함수로 최솟값을 구해 이를 arr에서 제거한 후 arr를 리턴한다.

### Q15. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12933
#### 문제: ![스크린샷 2021-02-12 오후 11 28 36](https://user-images.githubusercontent.com/60768642/107780475-1169e880-6d8a-11eb-8b90-05f18c822f6b.png)

#### my solution
```
def solution(n):
    n = list(str(n))
    new_n = sorted(n, reverse=True)
    res = "".join(new_n)
    return int(res)
```
#### 사고과정
1. 정렬을 위해 int -> str -> list로 바꿔준다.
2. 역정렬이므로 reverse=True옵션을 사용한 sorted 함수를 먹인다. 
3. list -> str -> int 으로 되돌리기 위해 join 함수, str() 함수를 활용한다.

### Q16. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12943
#### 문제:
![스크린샷 2021-02-12 오후 11 40 37](https://user-images.githubusercontent.com/60768642/107781870-bf29c700-6d8b-11eb-93c0-5d91bd872062.png)
#### my solution
```
def solution(num):
    if num == 1:
        return 0
    n = 0
    while num != 1:
        if n == 500:
            return -1
        if num % 2 == 0:
            num = num / 2
            n += 1
        else:
            num = (num * 3) + 1
            n += 1
    return n
```
#### 사고과정
1. 처음부터 1이 주어지면 바로 0을 리턴한다.
2. n = 0으로 할당해놓고 작업을 돌 떄 마다 +1일 해준다.
3. while문을 사용하여 실제 로직을 수행한다. 
4. n이 500이 되면 -1을 리턴한다.
5. while문을 빠져나오면 n을 리턴한다.


### Q17. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/68644
#### 문제:
![스크린샷 2021-02-12 오후 11 51 25](https://user-images.githubusercontent.com/60768642/107783136-41ff5180-6d8d-11eb-9abc-96b8101f08f4.png)
![스크린샷 2021-02-12 오후 11 51 32](https://user-images.githubusercontent.com/60768642/107783668-e1bcdf80-6d8d-11eb-8ec7-de05e365b6c0.png)

#### my solution
```
def solution(numbers):
    answer = []
    for index1 in range(len(numbers) - 1):
        for index2 in range(index1+1, len(numbers)):
            res = numbers[index1] + numbers[index2]
            if res not in answer:
                answer.append(res)
            
    return sorted(answer)
```
#### 사고과정
1. 결과값을 담을 빈리스트 answer을 만들고, 여기에 값들을 append해준다. 
제일 마지막엔 이 리스트를 sort해서 return해준다.
2. 이중 for문을 돌아야한다. 핵심은 이중 포문을 도는 조건문이다.
3. 돌면서, 두 값을 더한 결과가 answer에 있으면 넘어가고, 없으면 append해준다.

#### 다른 사람의 풀이
중복제거, 정렬해주는 방법을 이렇게도 할 수 있구나. 
 return sorted(list(set(answer)))
 
### Q18. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/64061
#### 문제:
<img width="687" alt="스크린샷 2021-02-13 오후 5 57 09" src="https://user-images.githubusercontent.com/60768642/107846167-fb5d3600-6e24-11eb-8b85-0615ae03c145.png">
<img width="684" alt="스크린샷 2021-02-13 오후 5 57 16" src="https://user-images.githubusercontent.com/60768642/107846171-fc8e6300-6e24-11eb-8c22-8298d89dffea.png">
<img width="685" alt="스크린샷 2021-02-13 오후 5 57 22" src="https://user-images.githubusercontent.com/60768642/107846172-fdbf9000-6e24-11eb-9e2b-3a6ac3429c7c.png">
<img width="701" alt="스크린샷 2021-02-13 오후 5 57 27" src="https://user-images.githubusercontent.com/60768642/107846173-fe582680-6e24-11eb-8d84-7a9850282a95.png">

#### my solution
```
def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for b in board:
            if b[i-1] != 0:
                moved_num = b[i-1]
                b[i-1] = 0
                if len(stack) == 0:
                    stack.append(moved_num)
                else:
                    if stack[-1] == moved_num:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(moved_num)
                break
    return answer
```
#### 사고과정
1. 인형들을 옮겨 닮을 빈 리스트를 하나 만든다.
2. 0으로 초기값을 설정해놓은 변수 하나를 두고, 같은 인형을 뽑을 때 마다 +2씩 해준다.
3. moves를 포문으로 돌면서, 그 안에서 board로 이중 포문을 돌며 로직을 수행한다.
4. 해당 인덱스에 0이 아닌 값이 존재할 경우, 그 값을 새로운 변수에 저장하고, 기존 인덱스 값을 0으로 만든다.
5. 옮겨 담을 리스트가 비었는지, 값이 있다면 마지막 값과 지금 뽑은 값이 같은지 확인하고, 같다면 pop으로 지워주고 +2를 해준다.
6. 같지 않다면 단순히 append해준다.
7. 더이상 포문을 돌면 안되므로 break한다.<br>
빡셌다.........

#### 다른 사람의 풀이
```
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
```
내 코드는 if else로 지저분한데, 이 사람 코드는 깔끔하다. <br>
댓글 중에 처음부터 리스트에 0값을 하나 넣어놓으면 len > 1인지를 검사 안해도 된다고 한 점이 인상깊었다.

