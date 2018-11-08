#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        res = ListNode(0)
        res_cur = res
        while cur and cur.next:
            tmp = cur.next.next
            res_cur.next = cur.next
            res_cur.next.next = cur
            res_cur.next.next.next = None
            res_cur = res_cur.next.next
            cur = tmp
        if cur:
            res_cur.next = cur

        return res.next
