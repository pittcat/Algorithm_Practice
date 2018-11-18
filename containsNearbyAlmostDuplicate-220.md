```
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        l = len(nums)
        for i in range(l):
            cur = nums[i]
            for j in range(i+1, l):
                if abs(nums[j] - cur) > t:
                    continue
                else:
                    if j - i <= k:
                        return True
                    else:
                        break

        return False
```

超时
