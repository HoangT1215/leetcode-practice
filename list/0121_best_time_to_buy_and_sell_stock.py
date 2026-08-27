"""LeetCode 121: Best Time to Buy and Sell Stock.

Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)

        # Naive solution: O(n^2).
        # for i in range(n - 1):
        #     maxprofit = max(
        #         maxprofit,
        #         max(prices[i + 1:]) - prices[i],
        #     )
        # return maxprofit

        # One-pass solution: retain the cheapest earlier buying price.
        min_past_price = prices[0]

        for i in range(n):
            min_past_price = min(min_past_price, prices[i])
            maxprofit = max(maxprofit, prices[i] - min_past_price)

        return maxprofit
