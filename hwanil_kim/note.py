class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(',
                ']': '[',
                '}': '{'
                }
        for chr in s:
            if chr in pair.values():
                stack.append(chr)
            else:
                if not stack:
                    return False
                left = stack.pop()
                if not pair[chr] == left:
                    return False
        if stack:
            return False
        return True








s = "()"
# s = "()[]{}"
# s = "(]"
# s = "{[]}"