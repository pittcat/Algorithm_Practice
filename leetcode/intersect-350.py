#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count_map, result = {}, []
        for i in nums1:
            if count_map.get(i) is None:
                count_map[i] = 0
            count_map[i] += 1

        for i in nums2:
            if count_map.get(i) is not None and count_map.get(i) > 0:
                result.append(i)
                count_map[i] -= 1

        return result
