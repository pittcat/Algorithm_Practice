#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return False
        first = 0
        last = len(nums) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if nums[mid] > nums[last]:
                if target < nums[mid] and target > nums[last]:
                    last = mid
                else:
                    first = mid
            elif nums[mid] < nums[last]:
                if target > nums[mid] and target <= nums[last]:
                    first = mid
                else:
                    last = mid
            else:
                last = last - 1

        if nums[first] == target or nums[last] == target:
            result = True
        else:
            result = False
        return result


moe = Solution()
re = moe.search([1, 2, 3, 1, 1], 0)
print(re)
