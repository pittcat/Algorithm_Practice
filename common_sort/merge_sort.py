#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def mergesort(self, seq):
        """
        :type seq: List[int]
        """
        if len(seq) <= 1:
            return seq
        mid = len(seq) // 2
        left = self.mergesort(seq[:mid])
        right = self.mergesort(seq[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        """
        :type left: List[int]
        :type right: List[int]
        """
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res += left[i:] or right[j:]
        return res


seq = [5, 3, 0, 6, 1, 4]
moe = Solution()
result = moe.mergesort(seq)
print(result, ...)
