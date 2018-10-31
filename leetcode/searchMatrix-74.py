#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: list
        :type target: int
        :return:
        """
        first = 0
        last = len(nums) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if nums[mid] > target:
                last = mid
            else:
                first = mid
        if nums[first] == target or nums[last] == target:
            return True
        else:
            return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]):
            return False
        row_length = len(matrix[0]) - 1
        col_length = len(matrix) - 1
        first_row = 0
        last_row = col_length
        result = False
        while last_row >= first_row:

            mid_row = (first_row + last_row) // 2
            if matrix[mid_row][0] <= target and matrix[mid_row][-1] >= target:
                result = self.search(matrix[mid_row], target)
                break
            elif target < matrix[mid_row][0]:
                last_row = mid_row - 1
                if last_row < 0:
                    break
            elif target > matrix[mid_row][-1]:
                first_row = mid_row + 1
                if first_row > col_length:
                    break

        return result


moe = Solution()
re = moe.searchMatrix([[1], [3]], 2)
print(re)
