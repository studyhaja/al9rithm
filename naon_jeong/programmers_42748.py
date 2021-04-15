'''
프로그래머스 코딩테스트 연습 - K번째수

https://programmers.co.kr/learn/courses/30/lessons/42748

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''


'''
solution1 함수
아직은 단순하고 쉬운 길밖에 몰라어 일단 이렇게 풀었다.
'''


def solution1(array, commands):
    result = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        sliced_array = array[i - 1:j]
        sliced_array.sort()
        result.append(sliced_array[k - 1])
    return result


'''
solution2 함수
이렇게도 값을 할당할 수 있구나.
'''


def solution2(array, commands):
    result = []
    for i, j, k in commands:
        sliced_array = array[i - 1:j]
        sliced_array.sort()
        result.append(sliced_array[k - 1])
    return result


'''
solution3 함수
^Pythonic^하게 list comprehension도 이용해봤다.
시간복잡도는 조금 올라갔다. (케이스마다 0.01ms 정도)
이렇게까지 리스트 컴프리헨션에 우겨넣어지는구나!
'''


def solution3(array, commands):
    return [sorted(array[i - 1:j])[k - 1] for i, j, k in commands]