#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [i for i in s.split(' ') if i != '']
        if res == []:
            return 0
        return len(res[-1])
