#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        res = []
        for idx in range(len(nums) - 1):
            res.append(nums[idx + 1] - nums[idx])

        return max(res)
