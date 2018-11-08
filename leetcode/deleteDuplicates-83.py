#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        cur = head
        cur_value = float('inf')
        while cur:
            if cur_value != cur.val:
                res.append(cur.val)
                cur_value = cur.val
            cur = cur.next
        res_node = ListNode(0)
        res_cur = res_node
        for i in res:
            res_cur.next = ListNode(i)
            res_cur = res_cur.next

        return res_node.next
