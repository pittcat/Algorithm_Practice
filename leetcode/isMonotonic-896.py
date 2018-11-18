#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sub = 0
        abs_sub = 0
        for i in range(len(A) - 1):
            sub += A[i + 1] - A[i]
            abs_sub += abs(A[i + 1] - A[i])
            if abs(sub) != abs_sub:
                return False

        return True
