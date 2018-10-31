#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        first = 0
        last = len(nums) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if nums[mid] < nums[last]:
                last = mid
            else:
                first = mid

        result = min(nums[first], nums[last])
        return result


# moe=Solution()
# re=moe.findMin([1])
# print(re)
