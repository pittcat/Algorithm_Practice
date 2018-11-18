#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def length(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        return length

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head_length = self.length(head)
        break_point = head_length // k
        if k == 0 or break_point == 0:
            return head
        b_count = 1
        cur = head
        res_node = ListNode(1)
        res_cur = res_node
        while cur and b_count <= break_point:
            prev = None
            count = 1
            while count <= k and cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                if count == 1:
                    prev_node = prev
                cur = tmp
                count += 1
            res_cur.next = prev
            res_cur = prev_node
            b_count += 1
        res_cur.next = cur
        return res_node.next
