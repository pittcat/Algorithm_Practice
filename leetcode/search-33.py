#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        first = 0
        last = len(nums) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if (target < nums[last] and nums[mid] > target and nums[mid] < nums[last]) or (
                    target > nums[last] and nums[mid] > target) or (
                    target > nums[last] and nums[mid] < target and nums[mid] < nums[last]):
                last = mid
            else:
                first = mid
        if nums[first] == target:
            result = first
        elif nums[last] == target:
            result = last
        else:
            result = -1
        return result

class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        first = 0
        last = len(nums) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if nums[mid] > nums[last]:
                if target < nums[mid] and target > nums[last]:
                    last = mid
                else:
                    first = mid
            else:
                if target > nums[mid] and target <= nums[last]:
                    first = mid
                else:
                    last = mid

        if nums[first] == target:
            result = first
        elif nums[last] == target:
            result = last
        else:
            result = -1
        return result

# moe = Solution()
# re = moe.search([], 5)
# print(re)
