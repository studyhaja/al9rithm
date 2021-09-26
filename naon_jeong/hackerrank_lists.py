'''
HackerRank Python Practice - Lists

https://www.hackerrank.com/challenges/python-lists/problem

Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
'''


'''
reverse를 arr[::-1]로 처리했는데, arr에 다시 대입을 해줘야 원본에 저장되는 거였다.
그거 말고는 딱히 막혔던 부분은 없었지만 이렇게 주먹구구라고..?싶기는 했다.
'''

if __name__ == '__main__':
    N = int(input())

result = []
for _ in range(N):
    command = list(map(str, input().split()))
    if command[0] == 'insert':
        result.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(result)
    elif command[0] == 'remove':
        result.remove(int(command[1]))
    elif command[0] == 'append':
        result.append(int(command[1]))
    elif command[0] == 'sort':
        result.sort()
    elif command[0] == 'pop':
        result.pop()
    else:
        result = result[::-1]


'''
명령어 패턴 파악해 코드 리팩토링
형변환 없이 문자열 그대로 연산할 수 있는 eval() 함수 이용
'''

if __name__ == '__main__':
    N = int(input())

result = []
for _ in range(N):
    command_set = list(map(str, input().split()))
    command = command_set[0]
    if command == 'print':
        print(result)
    else:
        eval('result.' + command + '(' + ','.join(command_set[1:]) + ')')
