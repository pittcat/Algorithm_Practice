#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l, r = (m - 1, n - 1)
        while l >= 0 and r >= 0:
            if nums1[l] > nums2[r]:
                nums1[l + r + 1] = nums1[l]
                l -= 1
            else:
                nums1[l + r + 1] = nums2[r]
                r -= 1
        if nums2[:r + 1] != []:
            nums1[:l + r + 2] = nums2[:r + 1]
