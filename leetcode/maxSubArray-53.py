#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution1:
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


class Solution2:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = [nums[0] for i in range(n)]
        for i in range(1, n):
            maxSum[i] = max(maxSum[i - 1] + nums[i], nums[i])
        return max(maxSum)
