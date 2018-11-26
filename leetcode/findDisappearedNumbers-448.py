#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(list(set(list(range(1, len(nums) + 1))) - set(nums)))
