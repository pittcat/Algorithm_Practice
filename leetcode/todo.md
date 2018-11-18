### 第二种解法665
```
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not len(nums) <= 1:
            return True
        count = 0
        for i in range(len(nums)-2):
            if nums[i+1]<nums[i]:
                count+=1
                if count>=2:
                    return False
                if i==0:
                    
```
### 解答127 

```

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def finddiff(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        i = 0
        diff = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                diff += 1

        return diff

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        res=[]
        cur_res=[]
        cur=[beginWord]
        while cur!=[]:
            cur_node=cur.pop(0)
            if cur_node:
                pass


moe = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
__import__('web_pdb').set_trace()
print(re, ...)
```

### 重写 46 47

### 第四题更好的解法
