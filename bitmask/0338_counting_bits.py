"""LeetCode 338: Counting Bits.

Problem: https://leetcode.com/problems/counting-bits/
Submission: https://leetcode.com/problems/counting-bits/submissions/2193457123/

Time complexity: O(n).
Output space complexity: O(n); O(1) additional space.
"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
