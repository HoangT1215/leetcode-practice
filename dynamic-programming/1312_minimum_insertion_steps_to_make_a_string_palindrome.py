"""LeetCode 1312: Minimum Insertion Steps to Make a String Palindrome.

Problem: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

Time complexity: O(n^2).
Space complexity: O(n^2).
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # dp[i][j]: minimum insertions to make s[i:j + 1] a palindrome.
        # Single-character and empty substrings need zero insertions.
        dp = [[0] * n for _ in range(n)]

        # Compute shorter substrings before longer ones.
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # The endpoints already match, so they need no insertion.
                    # Only the inner substring s[i + 1:j] remains to be solved.
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    # Insert s[i] after s[j] and solve s[i + 1:j + 1],
                    # or insert s[j] before s[i] and solve s[i:j].
                    # Each choice costs one insertion; take the cheaper one.
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
