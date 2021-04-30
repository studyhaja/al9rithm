'''
백준 온라인 저지 - 공유기 설치

https://www.acmicpc.net/problem/2110

도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
'''


'''
다른 사람 풀이를 참고해서 풀었다.
사실 min_distance = gap + 1, max_distance = gap - 1 대입 부분이 잘 이해가 안 된다.
일단 이해한 부분만 기술하자면...

집 좌표를 리스트 house에 저장한 후 오름차순으로 정렬한다.
최대한 많은 곳에서 와이파이를 사용할 수 있어야 하고, 인접한 두 공유기 사이가 가능한 멀어야 하므로 주어진 집 좌표 중 가장 앞에 위치한 집에는 무조건 공유기를 설치한다.
가장 앞에 있는 집에 공유기 1개를 설치했으므로 공유기 수(cnt)는 1부터 시작한다.

공유기를 설치할 수 있는 최소 거리(min_distance) 초기값은 1이므로 1을 지정하고,
최대 거리(max_distance) 초기값은 가장 뒤에 있는 집 좌표와 가장 앞에 있는 집 좌표의 차가 된다.

인접한 두 공유기 사이 거리(gap)는 우선 최소 거리와 최대 거리의 중간값으로 설정하고 검증을 시작한다.
만약 공유기가 설치해야 하는 수와 같거나 더 많이 설치되었다면 gap을 늘려서 검증을 반복한다.
다시 검증했을 때 설치해야 하는 수보다 적을 수 있으므로 result에 직전 gap 값을 저장해둔다.
'''

n, c = list(map(int, input().split()))

house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

min_distance = 1
max_distance = house[-1] - house[0]
result = 0

while min_distance <= max_distance:
    gap = (max_distance + min_distance) // 2
    value = house[0]
    cnt = 1
    for i in range(1, len(house)):
        if house[i] >= value + gap:
            value = house[i]
            cnt += 1

    if cnt >= c:
        min_distance = gap + 1
        result = gap
    else:
        max_distance = gap - 1

print(result)
