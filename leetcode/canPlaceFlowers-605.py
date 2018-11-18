#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        l = len(flowerbed)
        flowerbed.append(2)
        flowerbed.insert(0, 2)
        for idx in range(1, l + 1):
            right = flowerbed[idx + 1]
            left = flowerbed[idx - 1]
            if flowerbed[idx] != 1:
                if left != 1 and right != 1:
                    flowerbed[idx] = 1
                    count += 1

        return count >= n
