from itertools import combinations as cb

def solution(nums):
    answer = 0
    for i in cb(nums, 3):
        three_sum = sum(i)
        if is_prime(three_sum):
            answer += 1
    return answer


import math
def is_prime(num):
    """소수 여부 판별하는 함수"""
    res = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            res += 1
    if res > 1:
        return False
    return True



# def solution(nums):
#     answer = 0
#     for i in range(0, len(nums)-2):
#         for j in range(i+1, len(nums)-1):
#             for k in range(j+1, len(nums)):
#                 three_sum = nums[i] + nums[j] + nums[k]
#                 if is_prime(three_sum):
#                     answer += 1
#     return answer
#
#
# import math
# def is_prime(num):
#     """소수 여부 판별하는 함수"""
#     res = 0
#     for i in range(1, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             res += 1
#     if res > 1:
#         return False
#     return True
