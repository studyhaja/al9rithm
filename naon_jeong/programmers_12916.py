'''
프로그래머스 코딩테스트 연습 - 문자열 내 p와 y의 개수
https://programmers.co.kr/learn/courses/30/lessons/12916
'''

# 최초 풀
def solution(s):
    s = s.replace('P', 'p')
    s = s.replace('Y', 'y')

    p_cnt = s.count('p')
    y_cnt = s.count('y')

    if p_cnt == y_cnt:
        return True
    return False

# return을 더 간결하
def solution(s):
    s = s.replace('P', 'p')
    s = s.replace('Y', 'y')

    p_cnt = s.count('p')
    y_cnt = s.count('y')

    return p_cnt == y_cnt

# lower 내장함수 사용
def solution(s):
    return s.lower.count('p') == s.lower.count('y')

'''
고민점)
내장함수를 사용하지 않고 푸는 것이 알고리즘 테스트 취지에 더 맞는 것 아닌가? 
있는 내장함수를 최대한 사용하는 것이 현명한 것인가?
'''