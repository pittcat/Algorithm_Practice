#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        cur = head
        res = []
        res_node = ListNode(0)
        res_cur = res_node
        while cur:
            res.append(cur.val)
            cur = cur.next

        cut = res[m - 1:n]
        cut.reverse()
        res[m - 1:n] = cut
        for i in res:
            res_cur.next = ListNode(i)
            res_cur = res_cur.next

        return res_node.next


class Solution2:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        cur = head
        prev = None
        res_node = ListNode(1)
        res_cur = res_node
        while count <= n:
            if count < m:
                res_cur.next = cur
                res_cur = res_cur.next
                cur = cur.next
                count += 1
            else:
                tmp = cur.next
                cur.next = prev
                prev = cur
                if count == m:
                    prev_node = prev
                cur = tmp
                count += 1
        res_cur.next = prev
        prev_node.next = cur
        return res_node.next
