class Solution:
    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num) == 1:
                return num


a = Solution()
res = a.singleNumber([4,1,2,1,2])
print(res)