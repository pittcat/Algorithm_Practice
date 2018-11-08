#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        first = ListNode(0)
        cur_first = first
        cur_node = head
        while cur_node:
            if cur_node.val != val:
                cur_first.next = ListNode(cur_node.val)
                cur_first = cur_first.next
            cur_node = cur_node.next
        return first.next
