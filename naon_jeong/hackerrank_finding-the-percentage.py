'''
HackerRank Python Practice - Finding the percentage

https://www.hackerrank.com/challenges/finding-the-percentage/problem

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''


'''
딕셔너리 생성까지 미리 코드에 되어있어서 매우 편하게 풀었다 감사합니다...
query_name이 딕셔너리의 key고, 해당 key에 해당하는 value가 그 학생이 받은 점수 리스트다.
리스트 합을 리스트 크기로 나눈 뒤, 주어진 출력 포맷에 맞춰 소수점 두 자리까지 출력하도록 정규식을 추가했다.
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

scores = student_marks[query_name]
avg_score = sum(scores) / len(scores)
print('%0.2f' % avg_score)
