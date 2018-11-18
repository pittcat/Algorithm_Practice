#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = [root]
        run_list = []
        result = []
        next_queue = []
        while queue != []:
            c_node = queue.pop(0)
            run_list.append(c_node.val)
            if c_node.left:
                next_queue.append(c_node.left)
            if c_node.right:
                next_queue.append(c_node.right)

            if queue == []:
                result.append(run_list)
                queue = next_queue
                next_queue = []
                run_list = []
        result = [i[len(i) - 1] for i in result]
        return result

