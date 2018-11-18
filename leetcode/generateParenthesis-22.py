#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.getpath(n, n, res)
        return res

    def getpath(self, left, right, res, path=""):
        """
        :type left: int
        :type right: int
        :type path: str
        :type res:  list
        :rtype: List[str]
        """
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.getpath(left - 1, right, res, path + '(')
        if right > left:
            self.getpath(left, right - 1, res, path + ')')
