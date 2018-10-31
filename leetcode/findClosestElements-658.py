#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findIndex(self, nums, target):
        first = 0
        last = len(nums) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if nums[mid] > target:
                last = mid
            else:
                first = mid
        return [first, last]

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) is 0:
            return []
        index = self.findIndex(arr, x)
        first = index[0]
        last = index[1]
        list_k = []
        while k > 0:
            judge_value = abs(arr[first] - x) - abs(arr[last] - x)
            if judge_value <= 0:
                list_k.insert(0, arr[first])
                if first == 0:
                    clone_list = arr[last:last + k - 1]
                    list_k = list_k + clone_list
                    break

                first = first - 1
            else:
                list_k.append(arr[last])
                if last == len(arr) - 1:
                    clone_list = arr[first - k + 2:first + 1]
                    list_k = clone_list + list_k
                    break
                last = last + 1

            k -= 1
        return list_k


moe = Solution()
re = moe.findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9)
print(re)
