#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getResult(self, root):
        res = []

        if not root:
            res.append(None)
            return res
        else:
            res += self.getResult(root.left)
            res.append(root.val)
            res += self.getResult(root.right)
        return res

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res=self.getResult(root)

        return res[1:len(res)-1]
