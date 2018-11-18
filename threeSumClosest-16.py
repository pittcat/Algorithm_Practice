#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        idx = 0
        disdance = float('inf')
        while idx + 2 < len(nums):
            tmp = target - nums[idx]
            tmp_list = nums[idx + 1:]
            left = 0
            right = len(tmp_list) - 1
            while left < right:
                if tmp_list[left] + tmp_list[right] == tmp:
                    return target
                if abs(tmp - tmp_list[left] - tmp_list[right]) < disdance:
                    disdance = abs(tmp - tmp_list[left] - tmp_list[right])
                    result = nums[idx] + tmp_list[left] + tmp_list[right]
                if tmp_list[left] + tmp_list[right] > tmp:
                    right -= 1
                else:
                    left += 1

            idx += 1
        return result
