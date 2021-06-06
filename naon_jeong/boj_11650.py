'''
백준 온라인 저지 - 좌표 정렬하기

https://www.acmicpc.net/problem/11650

2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''


'''
리스트 내 튜플로 입력받아 람다함수로 정렬했다.
처음엔 튜플의 0번째 인덱스만을 기준으로 오름차순 정렬했더니 (1, 1)과 (1, -1)이 있을 때 정렬이 되지 않았다.
0번째 인덱스인 1끼리만 비교하고, 값이 같으니 정렬하지 않고 그냥 넘어간 모양.
그래서 0번째 인덱스를 첫 번째 기준으로, 1번째 인덱스를 두 번째 기준으로 정렬했다. 
'''

import sys


cnt = int(input())

points = []
for i in range(cnt):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.sort(key=lambda x: (x[0], x[1]))

for point in points:
    print(point[0], point[1])
