'''
프로그래머스 코딩테스트 연습 - 가운데 글자 가져오기
https://programmers.co.kr/learn/courses/30/lessons/12903
'''

def solution(s):
    if len(s) % 2 == 1:
        idx = len(s) // 2
        return s[idx]
    idx = (len(s) // 2) - 1
    return s[idx:idx+2]
