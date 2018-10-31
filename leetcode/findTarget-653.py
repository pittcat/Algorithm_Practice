#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def preorder(self, root):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = []
        if root:
            res += self.preorder(root.left)
            res.append(root.val)
            res += self.preorder(root.right)

        return res

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        numbers = self.preorder(root)
        left, right = (0, len(numbers) - 1)
        while left < right:
            if numbers[left] + numbers[right] == k:
                return True
            elif numbers[left] + numbers[right] < k:
                left += 1
            else:
                right -= 1
        return False
