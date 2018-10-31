#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        for (key, value) in nums_dict.items():
            if value > len(nums) // 2:
                result = key

        return result



