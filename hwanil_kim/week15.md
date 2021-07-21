## Q.48

#### 문제. https://programmers.co.kr/learn/courses/30/lessons/42578

#### 나의 풀이
- 의상 종류가 Key, 의상 이름이 value(list)인 dict를 만든다.
- 경우의 수 구하듯이 의상의 종류 수를 서로 곱해주면 된다.
- 이때, 의상을 안입는 경우도 있으므로 각 의상에 +1을 해준다.
- 하지만 아무것도 안입는 경우는 없으므로 전체 결과에서 -1을 해준다.
```
def solution(clothes):
    clothes_dict = dict()
    for cloth in clothes:
        if cloth[1] in clothes_dict:
        	clothes_dict[cloth[1]].append(cloth[0])
        else:
            clothes_dict[cloth[1]] = [cloth[0]]
    res = 1
    for k in clothes_dict.keys():
        res *= len(clothes_dict[k]) + 1
    return res - 1
```