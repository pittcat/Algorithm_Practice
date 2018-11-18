#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def levelOrder(self, root):
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
            result.append(c_node)
            if c_node.left is not None:
                next_queue.append(c_node.left)
            if c_node.right is not None:
                next_queue.append(c_node.right)
            if queue == []:
                final_result.append(result)
                result = []
                queue = next_queue
                next_queue = []

        return final_result

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        result_list = self.levelOrder(root)
        for i in result_list:
            index = 0
            while index + 1 < len(i):
                i[index].next = i[index + 1]
                index += 1
