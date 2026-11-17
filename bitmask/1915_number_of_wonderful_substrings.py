"""LeetCode 1915: Number of Wonderful Substrings.

Problem: https://leetcode.com/problems/number-of-wonderful-substrings/

Time complexity: O(10 * n) = O(n).
Space complexity: O(2**10) = O(1) for the fixed ten-letter alphabet.
"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counts = [0] * 1024
        counts[0] = 1

        mask = 0
        result = 0

        for char in word:
            # ord(char) - ord("a") maps 'a'...'j' to bit positions 0...9.
            # 1 << position selects that bit; XOR toggles it:
            # 0 -> 1 means the character count is odd; 1 -> 0 means even.
            mask ^= 1 << (ord(char) - ord("a"))

            # All character counts are even.
            result += counts[mask]

            # Exactly one character count is odd.
            for bit in range(10):
                # Flip one bit to find earlier prefix masks that differ only
                # in this letter's parity. Each such prefix gives a substring
                # ending here with exactly one odd character count.
                result += counts[mask ^ (1 << bit)]

            counts[mask] += 1

        return result
