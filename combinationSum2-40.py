#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(candidates)
        idx = 0
        record = []
        res = []
        self.dfs(nums, target, idx, record, res)
        return res

    def dfs(self, nums, target, idx=0, record=[], res=[]):
        cur_nums = nums[idx:]
        for i in range(len(cur_nums)):
            if target - cur_nums[i] == 0:
                record.append(cur_nums[i])
                copy_record = record.copy()
                if copy_record not in res:
                    res.append(copy_record)
            elif target - cur_nums[i] > 0:
                record.append(cur_nums[i])
                idx += 1
                self.dfs(nums, target - cur_nums[i], idx, record, res)
            else:
                return
            record.pop()
