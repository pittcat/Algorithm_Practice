#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        count_dict = {}
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
            if count_dict[i] == 2:
                count_dict[i] -= 1
                res.append(i)
        return res
