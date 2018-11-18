#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num_str = str(x)
        first_char = num_str[0]
        if first_char == '-':
            reverse_num_str = num_str[1:][::-1]
            result = -int(reverse_num_str)
        else:
            reverse_num_str = num_str[::-1]
            if reverse_num_str[0] == '0' and len(num_str) > 1:
                result = int(reverse_num_str[1:])
            else:
                result = int(reverse_num_str)

        if result > 2147483647 or result < -2147483648:
            return 0

        return result


moe = Solution()
moe_num = moe.reverse(0)
print(moe_num)
