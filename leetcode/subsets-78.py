#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = sorted(nums)
        res = [[]]
        self.dfs(nums, [], 0, res)

        return res

    def dfs(self, nums, path=[], index=0, res=[[]]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i in range(index, len(self.nums)):
            path.append(nums[i])
            res.append(path[:])
            self.dfs(nums, path, i + 1, res)
            path.pop()
