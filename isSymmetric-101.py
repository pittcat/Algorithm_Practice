#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetry(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(
            p.left, q.right) and self.isSameTree(p.right, q.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSameTree(root.left, root.right)
