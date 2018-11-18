#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        else:
            tmp = root.left
            root.left = root.right
            root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
