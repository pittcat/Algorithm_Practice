#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = []
        if root:
            res += self.inorder(root.left)
            res.append(root)
            res += self.inorder(root.right)
        return res

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        res = self.inorder(root)
        Sum = sum([i.val for i in res])
        for i in range(len(res)):
            tmp = res[i].val
            res[i].val += Sum - res[i].val
            Sum -= tmp
        return root
