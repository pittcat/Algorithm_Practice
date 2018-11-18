#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        char_dict = OrderedDict([(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'),
                                 (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'),
                                 (100, 'C'), (400, 'CD'), (500, 'D'),
                                 (900, 'CM'), (1000, 'M'), (2000, 'MM'),
                                 (3000, 'MMM')])
        #  python的时候直接使用字典不会乱序
        char_interval_list = list(char_dict.keys())
        init_num_length = len(str(num))
        num_str_list = []
        result_list = []
        while True:
            str_num_length = len(str(num))
            char_ele = num // pow(10, str_num_length - 1)

            num_str_list.append(char_ele * pow(10, str_num_length - 1))
            if len(num_str_list) == init_num_length:
                break
            num -= char_ele * pow(10, str_num_length - 1)
        for i in num_str_list:
            if char_dict.get(i):
                result_list.append(char_dict.get(i))
            else:

                for index in range(len(char_interval_list)):
                    if i > char_interval_list[
                            index] and i < char_interval_list[index + 1]:
                        break
                if i % char_interval_list[index] != 0:
                    result_list.append(
                        char_dict.get(char_interval_list[index]))
                    i -= char_interval_list[index]
                    index -= 2
                if i % char_interval_list[index] == 0:
                    ele_num = i // char_interval_list[index]
                    for j in range(ele_num):
                        result_list.append(
                            char_dict.get(char_interval_list[index]))

        return ''.join(result_list)


class Solution1(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        c = {
            0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            1: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            2: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            3: ["", "M", "MM", "MMM"]
        }
        roman = []
        roman.append(c[3][num // 1000 % 10])
        roman.append(c[2][num // 100 % 10])
        roman.append(c[1][num // 10 % 10])
        roman.append(c[0][num % 10])
        s = ''
        for i in roman:
            s = s + i
        return s


moe = Solution1()
re = moe.intToRoman(58)
print(re)
