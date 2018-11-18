#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_lst = s.split(" ")
        s_lst = [i for i in s_lst if i != ""]
        return len(s_lst)
