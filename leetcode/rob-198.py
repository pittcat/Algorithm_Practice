#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 2:
            return 0 if nums == [] else nums[0]
        res_lst = [nums[0], max(nums[0], nums[1])]
        for i in range(2, l):
            res_lst.append(max(res_lst[i - 1], res_lst[i - 2] + nums[i]))

        return res_lst[-1]
