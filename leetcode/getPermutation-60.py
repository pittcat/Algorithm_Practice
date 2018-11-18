#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def getfactorial(self, nums):
        res = 1
        i = 1
        while i <= nums:
            res *= i
            i += 1
        return res

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1, n + 1))
        res = []
        while n > 0:
            cur = self.getfactorial(n - 1)
            if k % cur == 0:
                idx = k // cur
            else:
                idx = k // cur + 1
            cur_res = nums.pop(idx - 1)
            res.append(cur_res)
            n -= 1
            k = k - (idx - 1) * cur

        return "".join([str(i) for i in res])
