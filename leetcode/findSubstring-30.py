#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        if n < 1:
            return []
        word_l = len(words[0])
        str_l = len(s)
        idx = 0
        res = []
        words_counter = Counter(words)
        while idx + word_l <= str_l:
            cur_word = s[idx:idx + word_l]
            if cur_word in words:
                first = idx
                last = idx + n * word_l
                if last > str_l:
                    return res
                cur_cut = s[first:last]
                cur_cut_lst = [
                    cur_cut[i:i + word_l]
                    for i in range(0, len(cur_cut), word_l)
                ]
                if Counter(cur_cut_lst) == words_counter:
                    res.append(first)
            idx += 1

        return res
