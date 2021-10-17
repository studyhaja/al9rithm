'''
HackerRank Python Practice - Find a string

https://www.hackerrank.com/challenges/find-a-string/problem

You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
'''


'''
startswith 함수를 이용한다.
for문을 돌면서 string을 앞에서부터 하나씩 끊어서 sub_string으로 시작하는지 여부를 검사한다.
'''

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
