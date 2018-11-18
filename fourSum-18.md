```
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        #  nums=sorted(nums)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[l] + nums[k] + nums[j] + nums[i] == target:
                            if sorted([nums[l], nums[k], nums[j],
                                       nums[i]]) not in res:
                                res.append(
                                    sorted(
                                        [nums[l], nums[k], nums[j], nums[i]]))

        return res
```

超时
