#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        final_result = []
        result = []
        if root is None:
            return final_result
        next_queue = []
        queue = [root]
        while queue != []:
            c_node = queue.pop(0)
            result.append(c_node.val)
            if c_node.left is not None:
                next_queue.append(c_node.left)
            if c_node.right is not None:
                next_queue.append(c_node.right)
            if queue == []:
                final_result.insert(0, result)
                result = []
                queue = next_queue
                next_queue = []

        return final_result
