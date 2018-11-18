#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res_node = ListNode(float('-inf'))
        res_cur = res_node
        cur = head
        while cur:
            tmp_cur = cur.next
            cur.next = None
            while res_cur.next:
                tmp = res_cur.next
                if res_cur.next.val > cur.val:
                    res_cur.next = cur
                    cur.next = tmp
                    break
                res_cur = tmp
            if res_cur.next is None:
                res_cur.next = cur

            cur = tmp_cur
            res_cur = res_node

        return res_node.next
