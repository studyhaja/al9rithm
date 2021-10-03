'''
HackerRank Python Practice - Design Door Mat

https://www.hackerrank.com/challenges/designer-door-mat/problem

Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
'''


'''
왕무식하게 풀기

.|. 패턴은 1, 3, 5, 7, 9 ... 수열에서 N // 2 번째 원소까지 증가하다가 WELCOME 라인을 만나고 다시 ... 9, 7, 5, 3, 1로 감소한다.
각 라인 중앙에 위치하는 .|. 패턴 외의 자리에는 하이픈(-)을 채워넣는다. .|. 패턴과 하이픈 개수 합은 M이어야 한다.
(즉, 하이픈(-) 수 = M - .|. 패턴 수 * 3)

WELCOME 라인에서는 WELCOME 일곱 자를 제외하고는 하이픈으로 채워야 하므로, (M - 7)개가 하이픈 수가 된다.

패턴이 증가할 때의 for문, WELCOME 라인, 패턴 감소 시 for문을 나눠서 출력한다.
'''

N, M = map(int, input().split())

for i in range(1, N, 2):
    print(('-' * ((M - 3 * i) // 2)), end="")
    print(('.|.' * i), end="")
    print(('-' * ((M - 3 * i) // 2)))

print('-' * ((M - 7) // 2) + 'WELCOME' + '-' * ((M - 7) // 2))

for i in range(N-2, 0, -2):
    print(('-' * ((M - 3 * i) // 2)), end="")
    print(('.|.' * i), end="")
    print(('-' * ((M - 3 * i) // 2)))


'''
center라는 파이썬 메소드가 있었다.

문자열.center(총 길이, 빈 공간 채울 문자)

이걸 사용하면 .|. 패턴 및 WELCOME 문자열과 가로 길이만 써줘도 빈 칸 개수가 자동 계산되어 그 공간에 하이픈을 채울 수 있다.
몹시 편리하다!!!
'''

N, M = map(int, input().split())
pattern = '.|.'
welcome = 'WELCOME'

upper = [print((pattern * i).center(M, '-')) for i in range(1, N, 2)]
print(welcome.center(M, '-'))
lower = [print((pattern * i).center(M, '-')) for i in range(N-2, 0, -2)]
