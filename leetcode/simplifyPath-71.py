#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_lst = path.split('/')
        stack = []
        for i in path_lst:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if stack != []:
                    stack.pop()
            else:
                stack.append(i)

        return '/' + '/'.join(stack)
