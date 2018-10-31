#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        next_queue = []
        result = []
        while queue != []:
            c_node = queue.pop(0)
            result.append(c_node.val)
            if c_node.left:
                next_queue.append(c_node.left)
            if c_node.right:
                next_queue.append(c_node.right)
            if queue == []:
                queue = next_queue
                next_queue = []
                if queue == []:
                    return result[0]
                result = []
