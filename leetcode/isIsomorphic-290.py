#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            if s_dict.get(s[i]) != t_dict.get(t[i]):
                return False
            s_dict[s[i]] = i
            t_dict[t[i]] = i
        return True
