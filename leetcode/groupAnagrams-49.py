#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_dict = {}
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            if tmp in res_dict:
                res_dict[tmp].append(i)
            else:
                res_dict[tmp] = [i]
        return list(res_dict.values())
