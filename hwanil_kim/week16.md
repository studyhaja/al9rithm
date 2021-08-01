## Q.50

#### 문제. https://leetcode.com/problems/single-number/
<img width="650" alt="Screen Shot 2021-08-01 at 10 16 09 PM" src="https://user-images.githubusercontent.com/86581178/127772257-7b15bdb3-4ae6-4563-bbd3-dae3648e0735.png">
<img width="652" alt="Screen Shot 2021-08-01 at 10 16 19 PM" src="https://user-images.githubusercontent.com/86581178/127772262-ea783b74-dfef-43e7-bc12-59e2dc838399.png">

#### 나의 풀이
```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num
                
        
```

