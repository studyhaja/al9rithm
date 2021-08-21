'''
HackerRank Python Practice - Write a function

https://www.hackerrank.com/challenges/write-a-function/problem

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

Given a year, determine whether it is a leap year.
If it is a leap year, return the Boolean True, otherwise return False.
'''


'''
윤년 판별하는 함수 작성하기.
난이도만 보면 쉬운 문제긴 한데, 조건문을 가장 효율적으로 짤 수 있는 방법을 고민해야 했다.
처참한 첫 번째 조건문.
'''

def is_leap1(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap

year = int(input())
print(is_leap1(year))


'''
통과는 하는데, 아무리 생각해도 이건 아닌 것 같아서 다시 시도함
'''

def is_leap2(year):
    leap = False

    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input())
print(is_leap2(year))


'''
함수 2도 지저분하다. 더 간단하게 할 수 있다.
400으로 나누어떨어지는 수면 당연히 100으로도, 4로도 나누어떨어지므로 굳이 구구절절 덧붙일 필요 없다.
마찬가지로, 100으로 나누어떨어지는 수는 4로도 나누어떨어지므로 and 이하 조건을 쳐내도 된다.
'''

def is_leap3(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input())
print(is_leap3(year))
