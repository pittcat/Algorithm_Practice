#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        l_height = self.maxDepth(root.left) + 1
        r_height = self.maxDepth(root.right) + 1
        if abs(l_height - r_height) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return True
