#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        path = []
        res = []
        self.dfs(s, path, res)
        return res

    def dfs(self, s, path=[], res=[]):
        if s == s[::-1]:
            path.append(s)
            res.append(path[:])
            path.pop()
        for i in range(1, len(s)):
            cut = s[:i]
            if cut == cut[::-1]:
                path.append(cut)
                self.dfs(s[i:], path, res)
                path.pop()
