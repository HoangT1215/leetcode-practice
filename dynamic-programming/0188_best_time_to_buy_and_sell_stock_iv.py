"""LeetCode 188: Best Time to Buy and Sell Stock IV.

Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Time complexity: O(n * k), or O(n) for the zero-fee unlimited-transactions shortcut
Space complexity: O(k), or O(1) for that shortcut
"""

import numpy as np


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        fee = 0  # version with fee
        if k == 0 or n < 2:  # basically no trade possible
            return 0

        # Summing positive daily changes is valid only when there is no fee.
        if fee == 0 and k >= n // 2:  # basically no transaction constraint
            return sum(
                max(0, prices[i] - prices[i - 1])
                for i in range(1, n)
            )

        profit = 0
        cash = [0] * (k + 1)
        hold = [float("-inf")] * (k + 1)

        # apply the cash and hold strategy backward
        for price in prices:
            for t in range(k, 0, -1):
                cash[t], hold[t] = (
                    max(cash[t], hold[t] + price - fee),
                    max(hold[t], cash[t - 1] - price),
                )

        return cash[k]
