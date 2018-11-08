#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join([str(i) for i in digits]))
        return [int(i) for i in str(num + 1)]
