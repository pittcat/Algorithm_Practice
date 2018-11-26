#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num = list(num)
        l = len(num)
        if k >= l or l == 0:
            return '0'
        res = []
        idx = 0
        while idx < l:
            while res != [] and int(num[idx]) < int(res[-1]) and k > 0:
                k -= 1
                res.pop()
            res.append(num[idx])
            idx += 1
        while k > 0:
            res.pop()
            k -= 1
        while res[0] == '0' and len(res) > 1:
            res.pop(0)
        if len(res) > l - k:
            res = res[:l - k + 1]
        return ''.join(res)
