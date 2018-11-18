#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = (0, len(nums) - 1)
        result = []
        while left < right:
            if nums[left] + nums[right] == target:
                if [-target, nums[left], nums[right]] not in result:
                    result.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        idx = 0
        target_sv = float('-inf')
        while idx + 2 < len(nums):
            target = -nums[idx]
            if target != target_sv:
                result += self.twoSum(nums[idx + 1:], target)
                target_sv = target
            idx += 1
        return result
