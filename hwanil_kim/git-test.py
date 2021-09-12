def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int("".join(nums)))

    return answer


# numbers = [6, 10, 2]
# numbers = [0, 0, 0]
# numbers = [3, 30, 34, 5, 9]
numbers = [i for i in range(30, 41)]
numbers.append(9)

print(solution(numbers))