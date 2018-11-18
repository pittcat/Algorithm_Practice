#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        record = []
        candidates = sorted(candidates)
        self.dfs(candidates, target, record, res)
        return res

    def dfs(self, nums, target, record=[], res=[]):
        """
        :type nums: List[int]
        :type record: List[int]
        :type target: int
        :type res: list
        """
        for i in nums:
            if target - i > 0:
                record.append(i)
                self.dfs(nums, target - i, record, res)
            elif target - i == 0:
                record.append(i)
                copy_record = sorted(record.copy())
                if copy_record not in res:
                    res.append(copy_record)
            elif target - i <= 0:
                return
            record.pop()
