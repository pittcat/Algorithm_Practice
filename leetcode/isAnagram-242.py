#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter


class Solution1:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)


class Solution2:
    def str2dict(self, s):
        """
        :type s: str
        :rtype: dict
        """
        s_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
        return s_dict

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.str2dict(s) == self.str2dict(t)


class Solution3:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(list(s)) == sorted(list(t))
