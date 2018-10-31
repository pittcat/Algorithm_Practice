#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        max_str = s[0]
        lengh = len(s)
        for i in range(1, lengh):
            font = i - 1
            behind = i
            while font >= 0 and behind < lengh and s[font] == s[behind]:
                font -= 1
                behind += 1
            if len(s[font + 1:behind]) > len(max_str):
                max_str = s[font + 1:behind]
            font = i - 1
            behind = i + 1
            while font >= 0 and behind < lengh and s[font] == s[behind]:
                font -= 1
                behind += 1
            if len(s[font + 1:behind]) > len(max_str):
                max_str = s[font + 1:behind]

        return max_str


moe = Solution()
re = moe.longestPalindrome("bb")
print(re)
