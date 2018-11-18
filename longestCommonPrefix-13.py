#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) == 0:
            return result
        elif len(strs[0]) == 0:
            return result
        elif len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            match = strs[0][0:i + 1]
            polar = True
            for k in strs[1:]:
                if match != k[0:i + 1]:
                    polar = False
                    break

            if polar:
                result = match
            else:
                break
        return result

