## Q.51

#### 문제. https://leetcode.com/problems/valid-parentheses

#### 나의 풀이
```
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
```


- stack을 이용해서 풀어야 한다.
- (, [, {를 left, ),],}를 right라고 했을 때, right가 오면 무조건 그 전에 같은 모양의 left가 left 중 가장 최근에 왔어야 한다.


## Q.52

#### 문제. https://leetcode.com/problems/longest-common-prefix

#### 나의 풀이
``` 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            flag = True
            for j in range(len(strs)):
                if not strs[0][:i+1] == strs[j][:i+1]:
                    flag = False
            if flag:
                res = strs[0][:i+1]
        return res
``` 