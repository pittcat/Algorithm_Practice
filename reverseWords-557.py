#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = 0
        s = list(s)
        for i in range(len(s)):
            if s[i].isspace() or i == len(s) - 1:
                if i == len(s) - 1:
                    right += 1
                tmp = s[left:right]
                s[left:right] = tmp[::-1]
                left = i + 1
                right = i + 1
            else:
                right += 1
        return "".join(s)
