#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution1:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                return True

        return False


class Solution2:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) == len(set(nums))
