#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i in range(len(s) - 1):
            if char_dict[s[i]] < char_dict[s[i + 1]]:
                sum -= char_dict[s[i]]
            else:
                sum += char_dict[s[i]]

        return sum + char_dict[s[len(s) - 1]]


