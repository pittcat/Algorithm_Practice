#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_dict = {}
        s = list(s)
        for i in s:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        res_count_lst = sorted([value for (key, value) in count_dict.items()])
        res_lst = []
        while res_count_lst != []:
            cur = res_count_lst.pop()
            for i in count_dict:
                if count_dict[i] == cur and (cur, i) not in res_lst:
                    res_lst.append((cur, i))
        return "".join([i[0] * i[1] for i in res_lst])
