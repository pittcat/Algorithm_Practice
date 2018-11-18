#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        count = 1
        res = '1'
        cur_count = 1
        while count < n:
            idx = 0
            cur_res = ''
            while idx < len(res):
                if idx == len(res) - 1 or res[idx] != res[idx + 1]:
                    cur_res += str(cur_count) + res[idx]
                    cur_count = 1
                else:
                    cur_count += 1
                idx += 1
            count += 1
            res = cur_res

        return res
