#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution1:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                if max_profit < i - min_price:
                    max_profit = i - min_price

        return max_profit


class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit_lst = [0] * len(prices)
        for i in range(1, len(prices)):
            profit_lst[i] = max(profit_lst[i - 1] + prices[i] - prices[i - 1],
                                0)
        return max(profit_lst)
