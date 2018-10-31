#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def GetTreelist(self, root):
        """
        :type root: TreeNode
        """
        res = []
        if root:
            res += self.GetTreelist(root.left)
            res.append(root.val)
            res += self.GetTreelist(root.right)
        return res

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        treelist = self.GetTreelist(root)
        return treelist[k - 1]
