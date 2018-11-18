#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        record = []
        idx = 1
        self.dfs(n, k, idx, record, res)
        return res

    def dfs(self, target, k, idx=1, record=[], res=[]):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        for i in range(idx, 10):
            if target - i == 0:
                record.append(i)
                copy_record = record.copy()
                if len(copy_record) == k and copy_record not in res:
                    res.append(copy_record)
            elif target - i > 0:
                record.append(i)
                idx += 1
                self.dfs(target - i, k, idx, record, res)
            else:
                return
            record.pop()
