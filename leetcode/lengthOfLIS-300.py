#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def binaryinsert(self, result, target):
        """
        :type result: list
        :type target: int
        """
        if result == []:
            result.append(target)
            return result
        first = 0
        last = len(result) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if result[mid] > target:
                last = mid
            else:
                first = mid
        if result[first] >= target:
            result[first] = target
        elif result[last] >= target and result[first] < target:
            result[last] = target
        else:
            result.append(target)
        return result

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is []:
            return 0
        res = []
        for i in nums:
            self.binaryinsert(res, i)

        return len(res)
