#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution1:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1 = nums.copy()
        nums2 = nums.copy()
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                nums1[i] = nums[i + 1]
                nums2[i + 1] = nums[i]
                break

        return nums1 == sorted(nums1) or nums2 == sorted(nums2)


