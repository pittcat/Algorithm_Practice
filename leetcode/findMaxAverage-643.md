```

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_val = float('-inf')
        for i in range(len(nums)):
            if i + k > len(nums):
                break
            tmp_max_val = sum(nums[i:i + k]) / k
            if tmp_max_val > max_val:
                max_val = tmp_max_val
        return max_val
```
超时
