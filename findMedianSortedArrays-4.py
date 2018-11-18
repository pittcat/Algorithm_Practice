#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        (i, j) = (0, 0)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        res += nums1[i:] or nums2[j:]
        k = len(res)
        if k % 2 == 1:
            return res[k // 2]
        else:
            return (res[k // 2 - 1] + res[k // 2]) / 2


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
