#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        result = 0
        if not root:
            return result
        queue = [root]
        next_queue = []
        c_result = []
        while queue != []:
            c_node = queue.pop(0)
            c_result.append(c_node.val)
            next_queue += c_node.children
            if queue == []:
                result += 1
                queue = next_queue
                next_queue = []
                c_result = []

        return result
