#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [[root, 1]]
        res = 1
        result_list = []
        next_queue = []
        while queue != []:
            c_node = queue.pop(0)
            result_list.append(c_node[1])
            if c_node[0].left:
                next_queue.append([c_node[0].left, c_node[1] * 2])
            if c_node[0].right:
                next_queue.append([c_node[0].right, c_node[1] * 2 + 1])
            if queue == []:
                res = max(res, result_list[-1] - result_list[0] + 1)
                result_list = []
                queue = next_queue
                next_queue = []
        return res
