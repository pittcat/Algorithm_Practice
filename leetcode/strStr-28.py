#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        first = needle[0]
        needle_len = len(needle)
        i = 0
        while i < len(haystack):
            if haystack[i] == first:
                if haystack[i:i + needle_len] == needle:
                    return i
                elif i + needle_len > len(haystack):
                    return -1

            i += 1

        return -1



