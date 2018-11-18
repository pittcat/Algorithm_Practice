#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        diameter = self.depth(root.left) + self.depth(root.right)
        return max(diameter, self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right))
