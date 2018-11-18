#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix[0])
        h = len(matrix)
        col_lst = []
        line_lst = []
        for i in range(h):
            for j in range(l):
                if matrix[i][j] == 0:
                    if j not in col_lst:
                        col_lst.append(j)
                    if i not in line_lst:
                        line_lst.append(i)
                    idx = i
                    while idx > 0:
                        matrix[idx - 1][j] = 0
                        idx -= 1
                elif j in col_lst:
                    matrix[i][j] = 0
            if line_lst != []:
                zero_line = line_lst.pop()
                matrix[zero_line] = l * [0]
