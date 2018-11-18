#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root, path):
        """
        :type path: list
        :type root: TreeNode
        """
        if not root:
            return path
        if root.left is None and root.right is None:
            path.append(root.val)
        if root.left:
            self.helper(root.left, path)
        if root.right:
            self.helper(root.right, path)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        path1, path2 = ([], [])
        self.helper(root1, path1)
        self.helper(root2, path2)
        if path1 == path2:
            return True
        else:
            return False
