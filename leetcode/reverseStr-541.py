#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        l = len(s)
        idx = 0
        while idx + 2 * k <= l:
            s[idx:idx + k] = reversed(s[idx:idx + k])
            idx += 2 * k
        if l - idx >= k and l - idx < 2 * k:
            s[idx:idx + k] = reversed(s[idx:idx + k])
        else:
            s[idx:] = reversed(s[idx:])

        return "".join(s)
