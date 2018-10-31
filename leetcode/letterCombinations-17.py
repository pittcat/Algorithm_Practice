#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        map_dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        length = len(digits)
        i = 0
        result = []
        while i < length:
            c_str = map_dict.get(int(digits[i]))
            if result == []:
                result += list(c_str)
            else:
                tmp = []
                for l in result:
                    for j in c_str:
                        tmp.append(l + j)
                result = tmp

            i += 1

        return result
