#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        max_val1 = nums[-1] * nums[-2] * nums[-3]
        max_val2 = nums[0] * nums[1] * nums[-1]
        return max(max_val1, max_val2)
