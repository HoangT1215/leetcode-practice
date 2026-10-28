"""LeetCode 122: Best Time to Buy and Sell Stock II.

Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Time complexity: O(n)
Space complexity: O(1)
"""


# Solution 1: Track increasing price segments (preserved for reference).
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         maxprofit = 0
#         pastprofit = 0
#         n = len(prices)
#         if n == 1:
#             return 0
#         start = 0
#         end = 0
#
#         for i in range(n - 1):
#             if prices[i] == prices[i + 1]:
#                 continue
#             elif prices[i] < prices[i + 1]:
#                 end = i + 1
#             else:
#                 pastprofit += prices[end] - prices[start]
#                 start, end = i + 1, i + 1
#         if prices[end] > prices[start]:
#             pastprofit += prices[end] - prices[start]
#         return pastprofit


# Solution 2: Dynamic programming with cash and hold states.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        cash, hold = 0, float("-inf")
        fee = 0  # fictional fee variable
        # code explanation: we have 3 states 1) buy 2) sell 3) hold
        # Clarification: buy/sell are actions; cash/hold are the two DP states.
        # we need 2 states to track the current cash and the current stock value we are holding
        # cash: net profit
        # hold: net cash value after buying stock
        # hold excludes the stock's current market value.

        for i in range(n):
            # cash = hold + price - fee mean sell
            # hold = cash - price means buy
            cash, hold = (
                max(cash, hold + prices[i] - fee),
                max(hold, cash - prices[i]),
            )

        return cash
