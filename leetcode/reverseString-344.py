#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        s_list.reverse()
        return "".join(s_list)
