### Q25. 
#### 문제링크: 없음
#### 문제: 이진 탐색 구현. element가 some_list에 있다면 index를, 없다면 None을 리턴하고, 이진 탐색 방법으로 구현하라.
```
def binary_search(element, some_list):
    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
```
결과

```
0
None
2
1
4
```
#### my solution
```
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        middle = (start_index + end_index) // 2
        if element == some_list[middle]:
            return middle
        elif element < some_list[middle]:
            end_index = middle - 1
        elif element > some_list[middle]:
            start_index = middle + 1
    return None
```
#### 사고과정
- 이진 탐색은 주어진 리스트의 중간 값을 먼저 확인하면서 범위를 좁혀가는 방법이다.
- 중간값은 시작 인덱스와 끝 인덱스를 더한 후 //2 연산을 해준 결과로 정한다.
- 중간값과 일치한다면 인덱스를 리턴, element가 중간값보다 큰지 작은지에 따라 범위를 좁혀가준다.
- 범위를 좁히는 방법은 중간값을 기준으로 끝 인덱스를 -1해주거나 시작 인덱스를 +1 해주는 방법을 사용한다.
- while문의 조건으로는, 시작 인덱스와 끝 인덱스가 교차하는 지점으로 잡아준다.

### Q26. 
#### 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12947
#### 문제:
#### my solution
```
```
#### 사고과정