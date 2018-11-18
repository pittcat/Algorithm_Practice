#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_list = list(str(x))
        clone_list = x_list.copy()
        clone_list.reverse()
        if x_list == clone_list:
            return True
        else:
            return False


class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x==int(str(x)[::-1]):
            return True
        else:
            return False
