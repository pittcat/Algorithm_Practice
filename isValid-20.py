#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == "":
            return True
        match_dict = {'}': '{', ')': '(', ']': '['}
        stack = []
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            else:
                if stack == [] or stack.pop() != match_dict[i]:
                    return False

        if stack == []:
            return True
        else:
            return False

        return True
