#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def intravel(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res.append(root.val)
            res += self.intravel(root.left)
            res += self.intravel(root.right)
        return res

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        res_list = self.intravel(root)
        res_dict = {}
        for i in res_list:
            if i in res_dict:
                res_dict[i] += 1
            else:
                res_dict[i] = 1

        max_index = max([value for (key, value) in res_dict.items()])
        for (key, value) in res_dict.items():
            if value == max_index:
                result.append(key)

        return result
