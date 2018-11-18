#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            positive = True
        else:
            positive = False
        dividend = abs(dividend)
        divisor = abs(divisor)

        first = divisor
        last = first + first
        count = 1
        run_result = 0

        if dividend < divisor:
            return 0
        while True:
            if last > dividend:
                run_result += count
                dividend = dividend - first
                first = divisor
                last = first + first
                count = 1
                if dividend >= first and dividend < last:
                    run_result += 1
                    break
                elif dividend < first:
                    break
            first = last
            last = last + last
            count = count + count

        if positive:
            result = run_result
        else:
            result = -run_result

        if result < -pow(2, 31) or result > pow(2, 31) - 1:
            return pow(2, 31) - 1

        return result


moe = Solution()

re = moe.divide(-2147483648, -1)
# re=moe.divide(12,5)
print(re)
