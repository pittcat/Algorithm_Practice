#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_dict = {}
        n = len(nums)
        res = []
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
            if nums_dict[i] > n / 3 and i not in res:
                res.append(i)
        return res
