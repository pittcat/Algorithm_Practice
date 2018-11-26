#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        res = []
        N -= 1
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - i):
                    node = TreeNode(0)
                    node.left = left
                    node.right = right
                    res.append(node)

        return res
