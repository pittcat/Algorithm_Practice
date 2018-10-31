#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
"""


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        while True:
            mid = (first + last) // 2
            if mid - 1 < 0:
                front = float('-inf')
            else:
                front = nums[mid - 1]
            if mid + 1 > len(nums) - 1:
                behind = float('-inf')
            else:
                behind = nums[mid + 1]

            if nums[mid] > front and nums[mid] > behind:
                return mid
            elif nums[mid] > front and nums[mid] < behind:
                first = mid + 1
            elif nums[mid] < front and nums[mid] > behind:
                last = mid - 1
            elif nums[mid] < front and nums[mid] < behind:
                first = mid + 1


moe = Solution()
re = moe.findPeakElement([1, 2, 1, 3, 5, 6, 4])
print(re)
