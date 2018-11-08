#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''.join([i for i in s if i.isalnum()]).lower()
        return res == res[::-1]
