'''
백준 온라인 저지 - 수 정렬하기 2

https://www.acmicpc.net/problem/2751

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''


'''
퀵정렬로 풀었더니 메모리 초과가 뜬다.
'''

import sys


cnt = int(input())
num_list = list()

for _ in range(cnt):
    n = int(sys.stdin.readline())
    num_list.append(n)


def recursive(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    left, right = list(), list()

    for idx in range(1, len(nums)):
        if nums[idx] < pivot:
            left.append(nums[idx])
        else:
            right.append(nums[idx])

    return recursive(left) + [pivot] + recursive(right)


for num in recursive(num_list):
    print(num)


'''
병합정렬로 풀었더니 통과했다.
'''

import sys


cnt = int(input())
num_list = list()

for _ in range(cnt):
    n = int(sys.stdin.readline())
    num_list.append(n)


def merge(left, right):
    result = list()
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result


def split(nums):
    if len(nums) <= 1:
        return nums

    medium = len(nums) // 2
    left = split(nums[:medium])
    right = split(nums[medium:])

    return merge(left, right)


for num in split(num_list):
    print(num)
