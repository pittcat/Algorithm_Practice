#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(
            p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            if t is None:
                return True
            else:
                return False
        return self.isSameTree(s, t) or self.isSubtree(
            s.left, t) or self.isSubtree(s.right, t)
