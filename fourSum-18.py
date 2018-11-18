#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        res = []
        cache = float('inf')
        for i in range(n):
            if nums[i] != cache:
                for j in range(i + 1, n):
                    tmp_target = target - nums[i] - nums[j]
                    tmp_nums = nums[j + 1:]
                    l, r = (0, len(tmp_nums) - 1)
                    while l < r:
                        if tmp_nums[l] + tmp_nums[r] == tmp_target:
                            tmp_list = [
                                nums[i], nums[j], tmp_nums[l], tmp_nums[r]
                            ]
                            if tmp_list not in res:
                                res.append(tmp_list)
                            l += 1
                            r -= 1
                        elif tmp_nums[l] + tmp_nums[r] > tmp_target:
                            r -= 1
                        else:
                            l += 1
                cache = nums[i]
        return res
