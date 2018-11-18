#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        sub_value = 0
        final = float("-inf")
        for i in range(len(nums)):
            if sub_value >= 0:
                max_val = sub_value + nums[i]
                sub_value += nums[i]
            else:
                max_val = nums[i]
                sub_value = nums[i]
            if max_val > final:
                final = max_val
        return final
