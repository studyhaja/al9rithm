'''
HackerRank Python Practice - sWAP cASE

https://www.hackerrank.com/challenges/swap-case/problem

You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
'''


'''
주어진 문장을 한 문자씩 소문자로 변환해보고,
원본과 일치하면 원본을 대문자로, 일치하지 않으면 소문자로 변환한다.
'''

def swap_case1(s):
    result = ''
    for c in s:
        if c == c.lower():
            result += c.upper()
        else:
            result += c.lower()
    return result


'''
swapcase()라는 빌트인 함수가 있었다. 허망
'''

def swap_case2(s):
    return s.swapcase()
