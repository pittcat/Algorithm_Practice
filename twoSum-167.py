#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution1:
    def binarysearch(self, nums, target):
        """
        :type nums: list
        :type target int
        """
        if nums == []:
            return None
        first = 0
        last = len(nums) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if nums[mid] > target:
                last = mid
            else:
                first = mid
        if nums[first] == target:
            return first
        elif nums[last] == target:
            return last
        else:
            return None

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        while index < len(numbers):
            judge_value = self.binary(numbers[index + 1:],
                                      target - numbers[index])
            if judge_value is not None:
                return [index + 1, index + judge_value + 2]
            index += 1


class Solution2:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = (0, len(numbers) - 1)
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
