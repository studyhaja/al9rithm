'''
프로그래머스 코딩테스트 연습 - 타겟 넘버

https://programmers.co.kr/learn/courses/30/lessons/43165

n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
'''


'''
DFS로 풀었다.
고민하다 답이 안 나와서 다른 사람 풀이를 보고 다시 풀었는데 그래도 아리까리했다.
알고리즘 개념을 배우고 나서 응용하는 것도 많은 연습이 필요하겠구나.
'''


def solution(numbers, target):
    answer = 0  # count 역할

    # 차례로 더한(뺀) 숫자를 append, pop을 반복해 총합을 구한다.
    queue = [(numbers[0], 0), (numbers[0] * -1, 0)]  # (해당 숫자, 인덱스 번호)
    while queue:
        num, idx = queue.pop()
        idx += 1
        if idx < len(numbers):
            queue.append((num + numbers[idx], idx))
            queue.append((num + numbers[idx] * -1, idx))
        else:
            if num == target:
                answer += 1

    return answer
