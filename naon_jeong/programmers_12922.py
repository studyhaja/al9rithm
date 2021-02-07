'''
프로그래머스 코딩테스트 연습 - 수박수박수박수박수박수?
https://programmers.co.kr/learn/courses/30/lessons/12922
'''

def solution(n):
    answer = ''
    i = 0
    while i < n:
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
        i += 1
    return answer


'''
오 이렇게 해도 되겠구나 했던 다른 사람 풀이
'''

def solution(n):
    answer = '수박' * n
    return answer[:n]