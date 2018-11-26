#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def judge(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] != '#':
                stack.append(s[idx])
            else:
                if stack != []:
                    stack.pop()
            idx += 1
        return stack

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.judge(S) == self.judge(T)
