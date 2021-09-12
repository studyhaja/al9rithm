## Q.60
#### 문제: https://programmers.co.kr/learn/courses/30/lessons/42746
#### 나의 풀이
``` 
def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int("".join(nums)))

    return answer
```

1. str형태의 숫자를 sort할 때 내부 동작을 이해할 필요가 있다.
2. 먼저 제일 앞자리를 놓고 비교한다. 
3. 따라서 [6, 10, 2]가 있을 때 앞자리는 6, 1, 2이므로 오름차순 기준 10, 2, 6으로 정렬된다.
4. input 숫자가 1000이하이기 때문에 같은 자리수로 놓고 비교하기 위해 문자열에 3을 곱해준다.
   1. 이 과정을 통해 6은 666, 10은 101010, 2는 222가 된다.
5. 이 상태에서 비교해주면 원하는 값이 나온다.
6. 후아...생각보다 어렵다.
