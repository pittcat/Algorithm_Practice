#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1s = list(num1)
        num2s = list(num2)
        l1 = len(num1s)
        l2 = len(num2s)
        sum = 0
        for i in range(l2):
            n2 = int(num2s[i]) * pow(10, l2 - 1 - i)
            for j in range(l1):
                n1 = int(num1s[j]) * pow(10, l1 - 1 - j)
                sum += n1 * n2
        return str(sum)
