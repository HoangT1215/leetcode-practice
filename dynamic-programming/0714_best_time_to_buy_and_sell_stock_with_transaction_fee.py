"""LeetCode 714: Best Time to Buy and Sell Stock with Transaction Fee.

Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        cash, hold = 0, -float("inf")
        if n < 2:  # basically no trade possible
            return 0
        else:
            for i in range(n):
                price = prices[i]
                cash, hold = (
                    max(cash, hold + price - fee),
                    max(hold, cash - price),
                )
            return cash
