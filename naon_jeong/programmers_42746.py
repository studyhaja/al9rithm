'''
프로그래머스 코딩테스트 연습 - 가장 큰 수

https://programmers.co.kr/learn/courses/30/lessons/42746

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
'''


'''
solution1 함수

문자열 정렬 방식을 기반으로 문제를 풀었다.
모두 정수로 이루어진 리스트 numbers 원소를 문자열로 변환한 뒤,
가장 앞자리부터 순서대로, 인덱스 0을 기준으로 정렬 -> 1을 기준으로 정렬 -> 2를 기준으로 정렬 -> 3을 기준으로 정렬하고
마지막에는 다시 정수로 변환했다가 return 형식에 맞게 문자열로 변환해 리턴한다.
numbers에 0이 여러 개 있다면 '000' 등으로 반환될 것이므로 '0'으로 반환하기 위해 정수로 변환하는 과정이 필요하다.

라고 단순하게 생각하고 막상 구현하려니, 인덱스 순으로 정렬할 때 인덱스 1이나 2가 없는 원소가 있어서 IndexError가 발생했다. (당연함)
이 부분은 해답을 못 찾다가 결국 다른 사람 풀이를 참조했다.
'''


def solution1(numbers):
    nums = list(map(str, numbers))
    sorted_nums = sorted(nums, reverse=True, key=lambda x: (x[0], x[1 % len(x)], x[2 % len(x)], x[3 % len(x)]))
    result = ''.join(sorted_nums)

    return str(int(result))


'''
solution2 함수

다른 기가막힌 풀이법.
리스트 내 원소 중 인덱스 0이 같지만 한 자릿수와 두 자릿수 이상이 섞여있을 때는 단순 정렬로 제대로 정렬되지 않는다.
예를 들어, '34', '3', '30'이 있을 때, reverse=True 조건으로만 정렬한다면 '34', '30', '3'이 된다.
따라서 원소가 최대 1000인 것을 이용해, 모든 원소를 세 자리 이상으로 뻥튀기한 결과값을 기준으로 정렬한다.

이런 생각은 어떻게 하는 거지 하하 신기하다
'''


def solution2(numbers):
    nums = list(map(str, numbers))
    sorted_nums = sorted(nums, reverse=True, key=lambda x: x*3)
    result = ''.join(sorted_nums)

    return str(int(result))

