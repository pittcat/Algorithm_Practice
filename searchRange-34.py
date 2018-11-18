#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        first = 0
        last = len(nums) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if target > nums[mid]:
                first = mid
            else:
                last = mid

        if nums[first] == target:
            index = first
        elif nums[last] == target:
            index = last
        else:
            return [-1, -1]

        first, last = (index, index)
        while True:
            if nums[first] != target:
                first += 1
                break
            if first == 0:
                break
            first -= 1
        while True:
            if nums[last] != target:
                last -= 1
                break
            if last == len(nums) - 1:
                break
            last += 1

        return [first, last]

