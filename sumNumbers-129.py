#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root, path, result):
        path.append(root)
        c_path = path.copy()
        if root.left is None and root.right is None:
            c_str = str(path[0].val)
            for i in path[1:]:
                c_str += str(i.val)
            num = int(c_str)
            result.append(num)

        if root.left:
            self.helper(root.left, path, result)
        if root.right:
            self.helper(root.right, c_path, result)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        result = []
        self.helper(root, [], result)
        final = sum(result)
        return final
