#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record_dict = {}
        for i in nums:
            if i in record_dict:
                record_dict[i] += 1
            else:
                record_dict[i] = 1

        for (key, value) in record_dict.items():
            if value == 1:
                return key


#  another solution
#  https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/136._single_number.md
