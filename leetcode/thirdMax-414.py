#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]
