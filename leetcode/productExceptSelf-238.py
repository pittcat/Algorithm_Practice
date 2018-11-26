#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l_nums = n * [1]
        for i in range(1, n):
            l_nums[i] = l_nums[i - 1] * nums[i - 1]
        tmp = 1
        res = []
        for i in range(n - 1, -1, -1):
            res.append(tmp * l_nums[i])
            tmp *= nums[i]
        res.reverse()
        return res
