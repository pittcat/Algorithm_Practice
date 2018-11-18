#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count_dict = {}
        for i in range(len(nums)):
            if nums[i] not in count_dict:
                count_dict[nums[i]] = i
            else:
                if i - count_dict[nums[i]] <= k:
                    return True
                else:
                    count_dict[nums[i]] = i

        return False
