#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        s = ""
        int_max = 2147483647
        int_min = -2147483648
        operater_nums = 0
        char_nums = 0
        result = 0
        for i in range(len(str)):
            if str[i].isspace() and char_nums == 0 and operater_nums == 0:
                continue
            if str[i] == '-' or str[i] == '+':
                if operater_nums == 0 and char_nums == 0:
                    s += str[i]
                    operater_nums += 1
                else:
                    break
            elif str[i].isdigit():
                s += str[i]
                char_nums += 1
            else:
                break

        if s == '-' or s == '+' or s == "":
            result = 0
        else:
            result = int(s)
        if result < -2147483648:
            result = int_min

        if result > int_max:
            result = int_max
        return result


moe = Solution()
re = moe.myAtoi("- 234")
print(re)
