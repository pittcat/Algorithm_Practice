#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
            else:

                index += 1

        return len(nums)
