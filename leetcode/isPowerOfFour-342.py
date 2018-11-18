#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 4 == 0:
            num /= 4
        return True if num == 1 else False
