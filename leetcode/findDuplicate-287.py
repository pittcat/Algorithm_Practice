#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
            if count_dict[i] > 1:
                return i
