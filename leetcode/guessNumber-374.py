#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n
        while last - first > 1:
            mid = (first + last) // 2
            judge_value = guess(mid)
            if judge_value is -1:
                last = mid
            else:
                first = mid

        if guess(first) is 0:
            result = first
        else:
            result = last
        return result
