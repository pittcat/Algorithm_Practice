#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) <= 1:
            return s
        s = list(s)
        left = 0
        right = len(s) - 1
        judge_lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while left <= right:
            if s[left] in judge_lst and s[right] in judge_lst:
                tmp = s[right]
                s[right] = s[left]
                s[left] = tmp
                left += 1
                right -= 1
            elif s[left] in judge_lst:
                right -= 1
            elif s[right] in judge_lst:
                left += 1
            else:
                left += 1
                right -= 1

        return ''.join(s)
