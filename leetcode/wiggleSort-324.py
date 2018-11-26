#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution1:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        snums = sorted(nums)
        mid_idx = size // 2
        if size % 2 == 1:
            mid_idx += 1
        l_nums = snums[:mid_idx][::-1]
        r_nums = snums[mid_idx:][::-1]
        nums[::2] = l_nums
        nums[1::2] = r_nums


class Solution2(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
