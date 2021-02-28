'''
프로그래머스 코딩테스트 연습 - 문자열 다루기 기본
https://programmers.co.kr/learn/courses/30/lessons/12918
'''

def solution(s):
    if len(s) in [4, 6]:
        try:
            s = int(s)
            return True
        except:
            return False
    return False