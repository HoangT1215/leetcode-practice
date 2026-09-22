"""LeetCode 122: Best Time to Buy and Sell Stock II.

Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprofit = 0
        pastprofit = 0
        n = len(prices)
        if n == 1:
            return 0
        start = 0
        end = 0

        for i in range(n - 1):
            if prices[i] == prices[i + 1]:
                continue
            elif prices[i] < prices[i + 1]:
                end = i + 1
            else:
                pastprofit += prices[end] - prices[start]
                start, end = i + 1, i + 1
        if prices[end] > prices[start]:
            pastprofit += prices[end] - prices[start]
        return pastprofit
