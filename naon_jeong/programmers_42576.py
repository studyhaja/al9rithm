'''
프로그래머스 코딩테스트 연습 - 완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576
'''

def solution(participant, completion):
    participant.sort()
    completion.sort()

    i = 0
    while(i<=len(completion)-1):
        if not participant[i] == completion[i]:
            break
        i += 1
    return participant[i]
