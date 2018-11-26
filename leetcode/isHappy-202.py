#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        str_n_lst = list(str(n))
        record_set = set()
        while True:
            sum_val = sum([int(i)**2 for i in str_n_lst])
            if sum_val == 1:
                return True
            elif sum_val in record_set:
                return False
            else:
                record_set.add(sum_val)
            str_n_lst = list(str(sum_val))
