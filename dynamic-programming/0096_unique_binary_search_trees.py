"""LeetCode 96: Unique Binary Search Trees.

Problem: https://leetcode.com/problems/unique-binary-search-trees/

Time complexity: O(n^2)
Space complexity: O(n)
"""


class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1

        # Recursive solution: correct, but exponentially slow without
        # memoization because it repeatedly solves the same subproblems.
        # total = 0
        # for i in range(n):
        #     total += self.numTrees(i) * self.numTrees(n - i - 1)
        # return total

        # Dynamic-programming solution.
        # dp[j] is the number of unique BSTs containing j ordered nodes.
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for number_of_nodes in range(2, n + 1):
            for left_size in range(number_of_nodes):
                right_size = number_of_nodes - left_size - 1
                dp[number_of_nodes] += dp[left_size] * dp[right_size]

        return dp[n]
