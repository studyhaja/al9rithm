'''
백준 온라인 저지 - 나이순 정렬

https://www.acmicpc.net/problem/10814

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
'''


'''
members 리스트에 튜플 형태로 (나이, 이름)을 저장한다. members 리스트 안 튜플들을 람다 함수를 이용해 나이순으로 정렬한다.
정렬 기준을 나이로만 지정했을 때, 같은 나이인 케이스는 정렬하지 않고 넘어가는데
기본적으로 리스트 내 튜플은 가입순으로 추가되어 있으므로 별도 정렬을 해주지 않아도 문제에서 요구한대로 나이가 같으면 가입순으로 정렬된다.
'''

member_cnt = int(input())
members = list()

for _ in range(member_cnt):
    age, name = input().split()
    members.append((int(age), name))

sorted_members = sorted(members, key=lambda x: x[0])

for member in sorted_members:
    print(member[0], member[1])
