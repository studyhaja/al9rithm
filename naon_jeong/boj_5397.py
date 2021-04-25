'''
백준 온라인 저지 - 키로거

https://www.acmicpc.net/problem/5397

창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다. 며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.
키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.
강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한줄로 이루어져 있고, 강산이가 입력한 순서대로 길이가 L인 문자열이 주어진다. (1 ≤ L의 길이 ≤ 1,000,000)
강산이가 백스페이스를 입력했다면, '-'가 주어진다. 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다.
화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다.
나머지 문자는 비밀번호의 일부이다. 물론, 나중에 백스페이스를 통해서 지울 수는 있다.
만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.
'''


'''
테스트케이스는 통과하는데 시간초과가 뜬다. 슬프다.
커서에 인덱스를 저장해서 해당 인덱스 번호 앞 문자를 삭제하거나, 커서 위치에 문자를 삽입하는 방식으로 구현했다. 
'''

testcase_cnt = int(input())

for _ in range(testcase_cnt):
    word = input()
    cursor = 0
    result = list()

    for char in word:
        if char == '<':
            if cursor > 0:
                cursor -= 1
        elif char == '>':
            if cursor < len(result):
                cursor += 1
        elif char == '-':
            if cursor > 0:
                del result[cursor - 1]
                cursor -= 1
        else:
            result.insert(cursor, char)
            cursor += 1

    print(''.join(result))


'''
커서를 사이에 둔 스택 2개가 있다고 가정하고 왼쪽 스택(prefix), 오른쪽 스택(suffix)을 생성했다.
- 왼쪽 방향키가 나오면 suffix에서 pop()한 data를 prefix에 append (단, suffix가 None이 아닐 때)
- 오른쪽 방향키가 나오면 prefix에서 pop()한 data를 suffix에 append (단, prefix가 None이 아닐 때)
- 일반 문자 삽입 시에는 prefix에 append
- prefix에 suffix를 넣고 출력하되, suffix는 뒤집어서 extend 해준다.
'''

testcase_cnt = int(input())

for _ in range(testcase_cnt):
    word = input()
    prefix = list()
    suffix = list()

    for char in word:
        if char == '<':
            if prefix:
                data = prefix.pop()
                suffix.append(data)
        elif char == '>':
            if suffix:
                data = suffix.pop()
                prefix.append(data)
        elif char == '-':
            if prefix:
                prefix.pop()
        else:
            prefix.append(char)

    prefix.extend(reversed(suffix))
    print(''.join(prefix))
