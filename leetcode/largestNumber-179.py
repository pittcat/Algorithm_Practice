#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def compare(self, n1, n2):
        """
        :type n1: int
        :type n2: int
        """
        num1 = int(str(n1) + str(n2))
        num2 = int(str(n2) + str(n1))
        if num1 > num2:
            return False
        else:
            return True

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums == [] or list(set(nums)) == [0]:
            return "0"
        for i in range(len(nums) - 1, -1, -1):
            for j in range(0, i):
                if self.compare(nums[j], nums[j + 1]):
                    tmp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = tmp
        return "".join([str(i) for i in nums])
