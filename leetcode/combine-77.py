#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        idx = 1
        record = []
        res = []
        self.dfs(n, k, idx, record, res)
        return res

    def dfs(self, n, k, idx=1, record=[], res=[]):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        for i in range(idx, n + 1):
            record.append(i)
            if len(record) == k:
                copy_record = record.copy()
                res.append(copy_record)
            else:
                idx += 1
                self.dfs(n, k, idx, record, res)
            record.pop()
