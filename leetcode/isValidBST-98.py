#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):

        res = []
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)

        return res

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = self.inorderTraversal(root)
        if res == [] and len(res) == 1:
            return True
        for i in range(len(res) - 1):
            if res[i + 1] <= res[i]:
                return False
        return True
