"""LeetCode 5: Longest Palindromic Substring.

Problem: https://leetcode.com/problems/longest-palindromic-substring/

Naive center expansion: O(n**2) time, O(1) auxiliary space.
Manacher's algorithm: O(n) time, O(n) auxiliary space.
Space bounds exclude the returned string.
"""


# Naive solution
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         start = 0
#         best_length = 0

#         for i in range(len(s)):
#             # Odd-length center (i, i) and even-length center (i, i + 1).
#             for left, right in ((i, i), (i, i + 1)):
#                 while (
#                     left >= 0
#                     and right < len(s)
#                     and s[left] == s[right]
#                 ):
#                     length = right - left + 1

#                     if length > best_length:
#                         start = left
#                         best_length = length

#                     left -= 1
#                     right += 1

#         return s[start:start + best_length]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Separators handle odd and even lengths uniformly.
        # Example: "abba" -> "#a#b#b#a#"
        t = "#" + "#".join(s) + "#"

        # p[i]: palindrome radius around position i in t.
        p = [0] * len(t)

        # Center and inclusive right boundary of the palindrome
        # that reaches furthest right so far.
        center = 0
        right = 0

        best_center = 0
        best_length = 0

        for i in range(len(t)):
            if i < right:
                mirror = 2 * center - i

                # Reuse the mirror's radius, but do not assume
                # anything beyond the known right boundary.
                p[i] = min(p[mirror], right - i)

            # Try expanding beyond the radius already established.
            while (
                i - p[i] - 1 >= 0
                and i + p[i] + 1 < len(t)
                and t[i - p[i] - 1] == t[i + p[i] + 1]
            ):
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

            # With this transformation, the radius equals the
            # palindrome's length in the original string.
            if p[i] > best_length:
                best_center = i
                best_length = p[i]

        # Convert the transformed position back to the original string.
        start = (best_center - best_length) // 2
        return s[start:start + best_length]
