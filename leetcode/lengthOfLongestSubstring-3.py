#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        point_f = 0
        if len(s) == 1:
            return 1
        while point_f < len(s):
            run_max_length = 1
            point_l = point_f + 1
            while point_l < len(s):
                if s[point_l] in s[point_f:point_l]:
                    point_f += s[point_f:point_l].index(s[point_l]) + 1
                    break
                point_l += 1
                run_max_length += 1

            if run_max_length > max_length:
                max_length = run_max_length
            if point_l >= len(s):
                break
            if len(s) - point_f <= max_length:
                break

        return max_length


#  moe = Solution()
#  Max_length = moe.lengthOfLongestSubstring("abcc")
#  print(Max_length)
