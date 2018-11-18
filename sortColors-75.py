#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_zero, count_one, count_two = 0, 0, 0
        for i in nums:
            if i == 0:
                count_zero += 1
            elif i == 1:
                count_one += 1
            else:
                count_two += 1
        nums[0:count_zero] = count_zero * [0]
        nums[count_zero:count_zero + count_one] = count_one * [1]
        nums[count_zero + count_one:] = count_two * [2]
