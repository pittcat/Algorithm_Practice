#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        first = 1
        last = num - 1
        while last - first > 1:
            mid = (first + last) // 2
            mid_value = mid * mid
            if mid_value > num:
                last = mid
            else:
                first = mid
        if first * first == num or last * last == num:
            return True
        else:
            return False

#
# moe = Solution()
# re = moe.isPerfectSquare(16)
# print(re)
