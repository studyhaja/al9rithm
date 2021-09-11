'''
HackerRank Python Practice - Find the Runner-up Score!

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
'''


'''
중복된 점수가 있을 수 있으므로 set형으로 바꾼 뒤 오름차순으로 정렬한다.
set 원소 중 마지막에서 두 번째 원소가 두 번째로 높은 점수일 것이므로 인덱스 -2번째 값을 출력한다.
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    score_set = sorted(set(arr))
    runner_up_score = score_set[-2]

    print(runner_up_score)
