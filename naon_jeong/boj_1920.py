'''
백준 온라인 저지 - 키로거

https://www.acmicpc.net/problem/1920

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.

모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.
'''


'''
리스트 탐색은 백퍼 시간초과 뜰 것 같아서 다른 방법을 궁리하다가 결국 못 찾았다.
역시나 시간초과
'''

target_length = int(input())
target_nums = list(map(int, input().split()))
search_length = int(input())
search_nums = list(map(int, input().split()))

for num in search_nums:
    if num in target_nums:
        print(1)
    else:
        print(0)


'''
문제풀이를 보니 방식은 완전히 같은데 target_nums를 리스트가 아닌 집합(set)으로 생성해줬다. 해보니까 된다. 무엇...?
찾아보니 set이 탐색 속도가 훨씬 빠르다고 한다.
'''

target_length = int(input())
target_nums = set(map(int, input().split()))
search_length = int(input())
search_nums = list(map(int, input().split()))

for num in search_nums:
    if num in target_nums:
        print(1)
    else:
        print(0)
