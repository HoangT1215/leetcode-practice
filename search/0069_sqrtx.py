"""LeetCode 69: Sqrt(x).

Problem: https://leetcode.com/problems/sqrtx/

Time complexity: O(log x)
Space complexity: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        current = x

        while current > low:
            if current * current > x:
                high = current
                current = (low + current) // 2
            else:
                low = current
                current = (high + current) // 2

        return current
