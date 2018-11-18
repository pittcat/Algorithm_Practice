#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[0]
