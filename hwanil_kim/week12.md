### Q45.
#### 문제.
- 링크: https://www.acmicpc.net/problem/10773
![스크린샷 2021-06-02 오전 9 44 25](https://user-images.githubusercontent.com/70195733/120407003-2f824580-c387-11eb-8c55-aea15ae0a808.png)
![스크린샷 2021-06-02 오전 9 44 31](https://user-images.githubusercontent.com/70195733/120407007-327d3600-c387-11eb-98c1-5f040736d873.png)

#### my_solution
```
length = int(input())
li = []

for i in range(length):
    num = int(input())
    if num != 0:
        li.append(num)
    else:
        li.pop()
print(sum(li))__
```

