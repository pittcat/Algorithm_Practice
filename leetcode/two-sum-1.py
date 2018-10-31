#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
'''
class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(list, item):
            low = 0
            high = len(list) - 1
            while low <= high:
                mid = (low + high) // 2
                guess = list[mid]
                if item == guess:
                    return True
                if item < guess:
                    high = mid - 1
                else:
                    low = mid + 1
            return None

        operation_numbers = sorted(nums.copy())
        while len(operation_numbers) > 1:
            other_num = target - operation_numbers[0]
            if binary_search(operation_numbers[1:], other_num):
                results_indexs = [
                    i for i, x in enumerate(nums)
                    if x == other_num or x == operation_numbers[0]
                ]
                break
            else:
                operation_numbers = [
                    e for e in operation_numbers
                    if e not in [operation_numbers[0], other_num]
                ]
        return results_indexs


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = sorted(nums)
        left, right = (0, len(tmp) - 1)
        while left < right:
            if tmp[left] + tmp[right] == target:
                if tmp[left] == tmp[right]:
                    l = nums.index(tmp[left])
                    r = nums[l + 1:].index(tmp[left])+l+1
                else:
                    l = nums.index(tmp[left])
                    r = nums.index(tmp[right])
                return sorted([l, r])
            elif tmp[left] + tmp[right] < target:
                left += 1
            else:
                right -= 1

