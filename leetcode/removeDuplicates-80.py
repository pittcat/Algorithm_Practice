#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        i = 0
        while i < len(nums):
            if nums[i] in count_dict:
                if count_dict[nums[i]] < 2:
                    count_dict[nums[i]] += 1
                else:
                    nums.pop(i)
                    i -= 1
            else:
                count_dict[nums[i]] = 1
            i += 1
        return len(nums)
