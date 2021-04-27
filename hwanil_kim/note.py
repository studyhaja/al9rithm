def solution(nums):
    answer = 0
    for i1 in range(0, len(nums) - 2):
        for i2 in range(1, len(nums) - 1):
            for i3 in range(2, len(nums)):
                three_sum = nums[i1] + nums[i2] + nums[i3]
                if is_prime(three_sum):
                    answer += 1
    return answer

    return answer


import math


def is_prime(num):
    res = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            res += 1
    if res > 1:
        return False
    return True


a = solution([1,2,7,6,4])
print(a)