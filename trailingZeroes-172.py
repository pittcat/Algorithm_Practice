#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        res = 0
        while n // 5 != 0:
            res += n // 5
            n //= 5

        return res
