#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution1:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        self.dfs(nums, sub)
        return self.res

    def dfs(self, Nums, subList):
        if len(subList) == len(Nums):
            self.res.append(subList[:])
        for m in Nums:
            if m in subList:
                continue
            subList.append(m)
            self.dfs(Nums, subList)
            subList.remove(m)


class Solution2:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            other = nums[:i] + nums[i + 1:]
            for j in self.permute(other):
                res.append([cur] + j)
        return res
