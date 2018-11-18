#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == "":
            return True
        upper = 0
        lower = 0
        for i in word:
            if i.isupper():
                upper += 1
            else:
                lower += 1
        if upper == 1 and word[0].isupper():
            return True
        return True if upper * lower == 0 else False
