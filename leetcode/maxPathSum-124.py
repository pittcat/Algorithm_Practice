#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.max_val = float("-inf")
        self.dfs(root, self.max_val)
        return self.max_val

    def dfs(self, root, max_val):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        cur_max = root.value
        left = self.dfs(root.left, self.max_val)
        left = left if left > 0 else 0
        right = self.dfs(root.right, self.max_val)
        right = right if right > 0 else 0
        self.max_val = max(left + right + cur_max, self.max_val)

        return max(left, right) + cur_max


from binarytree import build
values = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
root = build(values)
print(root, ...)
moe = Solution()
re = moe.maxPathSum(root)
print(re, ...)
