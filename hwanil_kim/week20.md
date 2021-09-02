## Q.58
#### 문제: https://programmers.co.kr/learn/courses/30/lessons/42888
#### 나의 풀이
``` 
def solution(record):
    answer = []
    uid_name_dict = dict()
    for row in record:
        split_row = row.split(' ')
        if len(split_row) > 2:
            uid = split_row[1]
            name = split_row[2]
            uid_name_dict[uid] = name
    for row in record:
        split_row = row.split(' ')
        status = split_row[0]
        uid = split_row[1]
        if status == "Enter":
            res = f"{uid_name_dict[uid]}님이 들어왔습니다."
            answer.append(res)
        elif status == "Leave":
            res = f"{uid_name_dict[uid]}님이 나갔습니다."
            answer.append(res)
    return answer
```


## Q.58
#### 문제: https://programmers.co.kr/learn/courses/30/lessons/42888
#### 나의 풀이
``` 
def solution(record):
    answer = []
    uid_name_dict = dict()
    for row in record:
        split_row = row.split(' ')
        if len(split_row) > 2:
            uid = split_row[1]
            name = split_row[2]
            uid_name_dict[uid] = name
    for row in record:
        split_row = row.split(' ')
        status = split_row[0]
        uid = split_row[1]
        if status == "Enter":
            res = f"{uid_name_dict[uid]}님이 들어왔습니다."
            answer.append(res)
        elif status == "Leave":
            res = f"{uid_name_dict[uid]}님이 나갔습니다."
            answer.append(res)
    return answer
```

## Q.59
#### 문제: https://programmers.co.kr/learn/courses/30/lessons/81301
#### 나의 풀이
``` 
def solution(s):
    mapping_data = {
        "zero" : 0,
        "one"  : 1,
        "two"  : 2,
        "three": 3,
        "four" : 4,
        "five" : 5,
        "six"  : 6,
        "seven": 7,
        "eight": 8,
        "nine" : 9
    }
    for k in mapping_data.keys():
        s = s.replace(k, str(mapping_data[k]))
    return int(s)
```
- replace함수를 이해하는 것이 핵심이다.
- replace함수의 첫 인자는 old 단어, 두번쨰 인자는 new 단어다.
- old를 찾아 new로 대체시키는 함수다.
- 이때 old, new는 모두 str이어야 한다.
- 만약 old가 기존 문자열에 없다면, 아무 일도 일어나지 않는다.
- replace 세 번째 인자로 int를 줄 수 있다.
- 이 인자는 old단어가 문장에 반복될시, 몇개까지 replace할지 정한다.
```

str = "this is string example....wow!!! this is really string"
print str.replace("is", "was")
print str.replace("is", "was", 3)

When we run above program, it produces following result −

thwas was string example....wow!!! thwas was really string
thwas was string example....wow!!! thwas is really string
```


