'''
백준 온라인 저지 - 트로피 진열

https://www.acmicpc.net/problem/1668

민식이는 “오민식”이라는 팀이름으로 수없이 많은 로봇대회를 우승했다. 따라서 민식이의 집에는 트로피가 많다.
민식이는 트로피를 어떤 선반 위에 올려놨다. 이 선반은 민식이의 방문을 열고 들어가자마자 선반의 왼쪽이 보인다.
다른말로 하자면, 뒤의 트로피가 앞의 트로피에 가려져 있다는 말이다.

안타깝게도, 높이가 큰 트로피가 높이가 작은 트로피의 왼쪽에 있다면, 높이가 작은 트로피는 큰 트로피에 가려서 보이지 않게 된다.
트로피는 자기의 앞에 (보는 사람의 관점에서) 자기보다 높이가 작은 트로피가 있을 때만 보이게 된다.
민식이는 선반을 180도 회전시켜서 트로피가 보이는 개수를 변하게 할 수도 있다.

선반위에 올려져 있는 트로피의 높이가 주어졌을 때, 왼쪽에서 봤을 때 보이는 개수와, 오른쪽에서 봤을 때 보이는 개수를 출력하는 프로그램을 작성하시오.
'''


'''
트로피 높이가 담긴 배열을 앞에서부터 한 번, 그리고 뒤에서부터 한 번 총 2번 순회한다.
어느 쪽에서 보든 직전에 가장 높았던 트로피보다 높아야 보일 것이므로, 높이 정보가 담긴 higher 배열에서 높이를 읽어와서 비교한다.
그 높이보다 높다면 higher 배열의 높이 정보를 갱신해주고 카운트 숫자에 1을 더해준다.
for문을 다 돈 뒤 change_cnt 배열에 저장한 트로피 개수를 출력한다.
'''

cnt = int(input())
trophies = [int(input()) for _ in range(cnt)]

higher = [trophies[0], trophies[-1]]
change_cnt = [1, 1]

for trophy in trophies:
    if trophy > higher[0]:
        higher[0] = trophy
        change_cnt[0] += 1

for trophy in trophies[::-1]:
    if trophy > higher[1]:
        higher[1] = trophy
        change_cnt[1] += 1

print(change_cnt[0])
print(change_cnt[1])
