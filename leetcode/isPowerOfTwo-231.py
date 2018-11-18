#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return True if n == 1 else False
