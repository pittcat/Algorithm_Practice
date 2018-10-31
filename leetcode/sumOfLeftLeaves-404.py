#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, path, root):
        if root.left is None and root.right is None:
            return 0
        if root.left:
            if root.left.left is None and root.left.right is None:
                path.append(root.left)
            self.helper(path, root.left)
        if root.right:
            self.helper(path, root.right)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        path = []
        self.helper(path, root)
        result = sum([i.val for i in path])
        return result
