#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 1 or numRows == 1 or len(s) <= numRows:
            return s
        restruct_str_list = []
        max_disdance = 2 * numRows - 2
        first_d = max_disdance
        for i in range(numRows):
            index = i
            restruct_str_list.append(s[index])

            if index == 0 or index == numRows - 1:
                polarity_dict = {True: max_disdance, False: max_disdance}
            else:
                first_d -= 2
                last_d = max_disdance - first_d
                polarity_dict = {True: first_d, False: last_d}

            judge_polarrity = True
            while index + polarity_dict[judge_polarrity] < len(s):
                restruct_str_list.append(
                    s[index + polarity_dict[judge_polarrity]])
                index = index + polarity_dict[judge_polarrity]
                judge_polarrity = not judge_polarrity

        return "".join(restruct_str_list)


moe = Solution()
s = "122asdasd"
numRows = 2
re = moe.convert(s, numRows)
print(re)
