#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                nums.pop(index)
            else:
                index += 1

        return len(nums)
