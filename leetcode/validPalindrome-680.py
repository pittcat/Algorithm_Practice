#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1] or len(s) == 1:
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                cur_l = s[:left] + s[left + 1:]
                cur_r = s[:right] + s[right + 1:]
                if cur_l == cur_l[::-1] or cur_r == cur_r[::-1]:
                    return True
                else:
                    return False
            else:
                left += 1
                right -= 1
