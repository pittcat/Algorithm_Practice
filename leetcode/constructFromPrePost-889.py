#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        idx = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:1 + len(post[:idx + 1])],
                                              post[:idx + 1])
        root.right = self.constructFromPrePost(pre[1 + len(post[:idx + 1]):],
                                               post[idx + 1:-1])
        return root
