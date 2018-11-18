#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = self.reverseList(slow)
        cur = head
        slow_cur = slow
        while slow_cur:
            if slow_cur.next is None:
                if cur.next:
                    cur.next = slow_cur
                break
            tmp_cur = cur.next
            cur.next = slow_cur
            slow_cur = slow_cur.next
            cur.next.next = tmp_cur
            cur = tmp_cur
