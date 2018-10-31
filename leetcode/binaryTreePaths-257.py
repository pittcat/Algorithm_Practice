#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
            ele_str = str(path[0].val)
            for i in path[1:]:
                ele_str += ("->" + str(i.val))
            result.append(ele_str)

        if root.left is not None:
            self.helper(root.left, path, result)
        if root.right is not None:
            self.helper(root.right, c_path, result)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        if root is None:
            return []
        result = []
        self.helper(root, [], result)
        return result
