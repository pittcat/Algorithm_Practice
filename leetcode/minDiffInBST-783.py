#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def InorderTraversal(self, root):
        res = []
        if root:
            res = self.InorderTraversal(root.left)
            res.append(root.val)
            res += self.InorderTraversal(root.right)
        return res

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = self.InorderTraversal(root)
        min_disdance = float('inf')
        first = 0
        last = 1
        while last < len(res):
            disdance = res[last] - res[first]
            if disdance < min_disdance:
                min_disdance = disdance

            first += 1
            last += 1

        return min_disdance
