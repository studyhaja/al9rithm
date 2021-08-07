class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = ""
        for i in range(len(strs[0])):
            flag = True
            for j in range(len(strs)):
                if not strs[0][:i+1] == strs[j][:i+1]:
                    flag = False
            if flag:
                res = strs[0][:i+1]
        return res


strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]

a = Solution()
a.longestCommonPrefix(strs)






