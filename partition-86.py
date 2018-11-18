#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        cur = head
        fir_node = ListNode(1)
        fir_cur = fir_node
        last_node = ListNode(x)
        last_cur = last_node
        while cur:
            if cur.val < x:
                fir_cur.next = ListNode(cur.val)
                fir_cur = fir_cur.next
            else:
                last_cur.next = ListNode(cur.val)
                last_cur = last_cur.next

            cur = cur.next
        fir_cur.next = last_node.next
        return fir_node.next


class Solution2:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        cur = head
        fir_node = ListNode(1)
        fir_cur = fir_node
        last_node = ListNode(x)
        last_cur = last_node
        while cur:
            tmp = cur.next
            cur.next = None
            if cur.val < x:
                fir_cur.next = cur
                fir_cur = fir_cur.next
            else:
                last_cur.next = cur
                last_cur = last_cur.next

            cur = tmp
        fir_cur.next = last_node.next
        return fir_node.next
