#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == p.val or root.val == q.val or (
                root.val > min(p.val, q.val) and root.val < max(p.val, q.val)):
            res = root
        if root.val > max(p.val, q.val):
            res = self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            res = self.lowestCommonAncestor(root.right, p, q)

        return res
