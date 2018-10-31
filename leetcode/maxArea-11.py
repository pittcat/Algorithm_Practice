#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        Area = 0
        while right > left:
            Width = right - left
            Height = min(height[left], height[right])
            area = Width * Height
            if area > Area:
                Area = area
            if height[left] >= height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1

        return Area


moe = Solution()
re = moe.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(re)
