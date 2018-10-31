#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def calculate(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        if root.val == sum:
            return 1 + self.calculate(root.left, 0) + self.calculate(
                root.right, 0)
        else:
            sum -= root.val
        return self.calculate(root.left, sum) + self.calculate(root.right, sum)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return 0
        return self.calculate(root, sum) + self.pathSum(
            root.left, sum) + self.pathSum(root.right, sum)
