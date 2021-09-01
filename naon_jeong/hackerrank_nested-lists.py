'''
HackerRank Python Practice - Nested Lists

https://www.hackerrank.com/challenges/nested-list/problem

Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
'''


'''
이렇게 장황하게 쓰는 게 맞나...?

lowest score가 2개 이상 있을 수 있으므로,
second lowest score라고 해서 반드시 sorted records의 1번쨰 인덱스에 해당하는 값은 아닐 것이다.
(lowest score가 2개 있으면 sorted records의 2번째 인덱스에 해당하는 값이 second lowest score가 됨)


'''

records = []

if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
            
        
sorted_records = sorted(records, key = lambda x : (x[1], x[0]))

lowest_score = sorted_records[0][1]
lowest_count = 0

for i in range(len(records)):
    if sorted_records[i][1] == lowest_score:
        lowest_count += 1
        
if lowest_count == 1:
    second_lowest_score = sorted_records[1][1]
else:
    second_lowest_score = sorted_records[lowest_count][1]
    
for i in range(len(records)):
    if sorted_records[i][1] == second_lowest_score:
        print(sorted_records[i][0])


'''
set을 이용하면 되는구나!
'''

records = list()
scores = set()

if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.add(score)
        
sorted_records = sorted(records, key = lambda x : (x[1], x[0]))
sorted_scores = sorted(scores)
second_lowest_score = sorted_scores[1]

for i in range(len(records)):
    if sorted_records[i][1] == second_lowest_score:
        print(sorted_records[i][0])
