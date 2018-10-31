#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution1(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.children:
            return [root.val]
        result = [root.val]
        for child in root.children:
            result += self.preorder(child)
        return result


class Solution2(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.children:
                curr.children.reverse()
                stack += curr.children
        return result
