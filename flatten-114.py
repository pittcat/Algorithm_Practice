#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def pretraversal(root):
            res = []
            if root:
                res.append(root)
                res += pretraversal(root.left)
                res += pretraversal(root.right)

            return res

        if root is None:
            return
        res = pretraversal(root)
        length = len(res)
        i = 0
        while i < length - 1:
            res[i].left = None
            res[i].right = res[i + 1]
            i += 1

        res[-1].left = None
        res[-1].right = None
