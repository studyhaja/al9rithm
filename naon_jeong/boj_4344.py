'''
백준 온라인 저지 - 평균은 넘겠지

https://www.acmicpc.net/problem/4344

첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
'''


'''
원시적으로 풀었다.
점수를 리스트로 입력받고, for문을 돌려서 평균을 구한 다음에 다시 for문을 돌려 리스트의 점수와 비교해 평균을 넘는 점수가 몇 개인지 셌다.
round 함수를 써서 반올림했더니 40.000%처럼 0으로 떨어지는 숫자는 40.0%이 되었다. format 함수를 써서 소수점 3자리로 맞춰줬다. 

참고) round 함수를 썼을 때
result = round((over_avg / len(scores)) * 100, 3)
print(str(result) + '%')
'''

case_cnt = int(input())

for i in range(case_cnt):
    scores = list(map(int, input().split()))
    score_cnt = scores[0]
    scores = scores[1:]
    average = sum(scores) / len(scores)
    over_avg = 0
    for score in scores:
        if score > average:
            over_avg += 1
    result = format((over_avg / len(scores)) * 100, '.3f')
    print(result + '%')
