#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = [[]]
        self.dfs(nums, [], 0, res)
        return res

    def dfs(self, nums, path=[], index=0, res=[[]]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i in range(index, len(nums)):
            path.append(nums[i])
            if path not in res:
                res.append(sorted(path[:]))
            self.dfs(nums, path, i + 1, res)
            path.pop()
