'''
백준 온라인 저지 - 벌집

https://www.acmicpc.net/problem/2292

중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다.
숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오.
예를 들면, 13까지는 3개, 58까지는 5개를 지난다.
'''


'''
수학으로 풀어보자 마음먹고 풀었더니 조금 의아한 풀이가 나오긴 했다.

벌집 한 겹을 한 그룹으로 묶어서 '단계'로 지칭한다.
입력으로 주어진 방까지 가기위해 거쳐야 하는 방 수는 입력으로 주어진 방이 속한 벌집 단계 수와 같다.

벌집 각 단계에 해당하는 수 중 마지막 수는 1 - 7 - 19 - 37 - 61 - ... 로,
이 수열을 점화식으로 만들면 fn = fn-1 + 6(n-1) 이 된다.
이것을 일반항으로 만들면 fn = 3n(n-1) + 1 = 3n^2 - 3n + 1 이 된다.

입력받는 숫자 N은 수열에 해당하는 수거나 수열의 각 수 사이에 위치한 수이므로,
일반항을 이용해 만든 이차방정식의 해보다 크거나 같으면서 가장 작은 정수가 N이 벌집에서 몇 단계에 있는지 나타내는 수가 된다.

이를 식으로 써보면,
3n^2 - 3n + 1 = N
3n^2 - 3n + (1-N) = 0
인 이차방정식을 만들 수 있고, 이를 근의 공식으로 풀어 해를 구한 뒤, 구한 해를 천장함수에 넣어 최종 값을 도출한다.
이차방정식 해는 2개지만 여기서는 양의 실수를 대상으로 하므로 두 해 중 더 큰 값을 max 함수로 뽑아냈다.   
'''


import math

N = int(input())
a = 3
b = -3
c = (1-N)

n = max(((-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)), ((-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)))
print(math.ceil(n))
