#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        slow = fast = pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)

    def merge(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        res_node = ListNode(1)
        res_cur = res_node
        first = h1
        last = h2
        while first and last:
            if first.val < last.val:
                res_cur.next = first
                first = first.next
            else:
                res_cur.next = last
                last = last.next
            res_cur = res_cur.next

        res_cur.next = first or last

        return res_node.next

