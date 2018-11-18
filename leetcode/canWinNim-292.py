#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)
