#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        init_sum = sum(nums[0:k])
        max_val = init_sum / k
        for i in range(1, len(nums)):
            if i + k > len(nums):
                break
            init_sum = init_sum - nums[i - 1] + nums[i + k - 1]
            tmp_max_val = init_sum / k
            if tmp_max_val > max_val:
                max_val = tmp_max_val
        return max_val
