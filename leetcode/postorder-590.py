#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.children:
            return [root.val]
        result = []
        for children in root.children:
            result += self.postorder(children)

        result.append(root.val)
        return result
