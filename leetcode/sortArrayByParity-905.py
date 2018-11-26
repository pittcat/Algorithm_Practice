#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd, even = [], []
        for i in A:
            if i % 2 == 1:
                odd.append(i)
            else:
                even.append(i)

        return sorted(even) + sorted(odd)
