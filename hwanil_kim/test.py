n = int(input())
cnt = 1
stack = []
res = []

for i in range(n):
    data = int(input())
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        res.append('+')
    if stack[-1] == data:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        exit(0)
print('\n'.join(res))



