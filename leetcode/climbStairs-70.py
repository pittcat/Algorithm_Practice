#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_dict = {0: 1, 1: 1}
        for i in range(2, n + 1):
            n_dict[i] = n_dict[i - 1] + n_dict[i - 2]
        return n_dict[n]
