#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        final = []
        self.helper(root, [], result)
        for i in result:
            t_sum = 0
            for k in i:
                t_sum += k
            if t_sum == sum:
                final.append(i)
        return final

    def helper(self, root, path, result):
        path.append(root)
        c_path = path.copy()
        if root.left is None and root.right is None:
            result.append([i.val for i in path])

        if root.left is not None:
            self.helper(root.left, path, result)
        if root.right is not None:
            self.helper(root.right, c_path, result)
