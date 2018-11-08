#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next

        return res == res[::-1]
