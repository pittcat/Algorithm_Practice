#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
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
        polar = True
        while queue != []:
            c_node = queue.pop(0)
            result.append(c_node.value)
            if c_node.left is not None:
                next_queue.append(c_node.left)
            if c_node.right is not None:
                next_queue.append(c_node.right)

            if queue == []:
                if not polar:
                    result.reverse()
                final_result.append(result)
                result = []
                queue = next_queue
                next_queue = []
                polar = not polar

        return final_result
