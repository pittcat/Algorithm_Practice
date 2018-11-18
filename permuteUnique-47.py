#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            other = nums[:i] + nums[i + 1:]
            for j in self.permuteUnique(other):
                if [cur] + j not in res:
                    res.append([cur] + j)
        return res
