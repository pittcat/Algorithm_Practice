#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        first = 1
        last = n
        while last - first > 1:
            mid = (first + last) // 2
            mid_value = 2 * n - mid * mid - 3 * mid
            if mid_value > 0:
                first = mid
            else:
                last = mid
        if 2 * n - first * first - 3 * first <= 0:
            result = first
        elif 2 * n - last * last - 3 * last <= 0:
            result = last

        return result

# moe = Solution()
# re = moe.arrangeCoins(2)
# print(re)
