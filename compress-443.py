#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1:
            return len(chars)
        cur = chars[0]
        count = 1
        idx = 0
        i = 1
        while i < len(chars):
            if chars[i] == cur:
                count += 1
            elif chars[i] != cur or i == len(chars) - 1:
                tmp = chars[i]
                if i==len(chars)-1:
                    i+=1
                if count > 1:
                    chars[idx:i] = [cur] + list(str(count))
                    tmp_l = len([cur] + list(str(count)))
                else:
                    chars[idx:i] = [cur]
                    tmp_l = len([cur])
                cur = tmp
                count = 1
                idx += tmp_l
                i = idx
            i += 1

        return len(chars)
