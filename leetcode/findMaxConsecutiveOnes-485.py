#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        Max = 0
        Run_max = 0
        index = 0
        while index < len(nums):
            if nums[index] == 1:
                Run_max += 1
            if index == len(nums) - 1 or nums[index] == 0:
                Max = max(Max, Run_max)
                Run_max = 0
            index += 1

        return Max
