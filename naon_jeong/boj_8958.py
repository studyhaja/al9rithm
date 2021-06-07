'''
백준 온라인 저지 - OX퀴즈

https://www.acmicpc.net/problem/8958

"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''


'''
다른 사람 풀이를 보니까 아차 했던 문제.
늘 그렇지만 답을 보고 나면 이걸 왜 머리를 싸매고 있었을까, 이 방법을 왜 생각 못했을까 이러고 있다.

OX로 이루어진 답안을 입력받고,
O를 만나면 점수에 지금까지 누적된 점수를 더해주고, 누적 점수에 1을 다시 더해준다.
X를 만나면 누적 점수를 1로 초기화한다. 
'''

import sys


cases = int(input())

for i in range(cases):
    answers = sys.stdin.readline()
    score = 0
    accumulate = 1
    for answer in answers:
        if answer == 'O':
            score += accumulate
            accumulate += 1
        else:
            accumulate = 1
    print(score)
