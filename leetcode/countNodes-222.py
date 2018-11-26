#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def height(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height = 0
        while root:
            height += 1
            root = root.left
        return height

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l_h = self.height(root.left)
        r_h = self.height(root.right)
        nodes = 0
        if l_h == r_h:
            nodes = 2**l_h - 1 + 1 + self.countNodes(root.right)
        else:
            nodes = 2**r_h - 1 + 1 + self.countNodes(root.left)

        return nodes
