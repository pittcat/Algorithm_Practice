#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res.append(root.val)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)

        return res

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.preorderTraversal(root)
        res = sorted(list(set(res)))
        if len(res) < 2:
            return -1
        else:
            return res[1]
