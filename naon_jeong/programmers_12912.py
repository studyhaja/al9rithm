'''
프로그래머스 코딩테스트 연습 - 두 정수 사이의 합
https://programmers.co.kr/learn/courses/30/lessons/12912

두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

- a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
- a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
- a와 b의 대소관계는 정해져있지 않습니다.
'''


'''
solution1 함수
O(1)을 노리고 1부터 n까지 합을 구하는 공식인 (n(n+1))/2를 이용했다.
'''


def solution1(a, b):
    if a == b:
        return a
    elif a < b:
        return ((a + b) * ((b - a) + 1)) // 2
    return ((a + b) * (a - b + 1)) // 2


'''
solution2 함수
절대값을 이용한 방법도 있었다. 속도, 공간 모두에서 크게 차이는 안 났다.
'''


def solution2(a, b):
    if a == b:
        return a
    return ((a + b) * (abs(b - a) + 1)) // 2


'''
solution3 함수
다른 사람 풀이 가장 상위에 있던 것을 돌려봤더니 위 방식보다 속도면에서 불리했다.
'''


def solution3(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
