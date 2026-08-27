"""LeetCode 3: Longest Substring Without Repeating Characters.

Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time complexity: O(n)
Space complexity: O(min(n, alphabet size))
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Test cases.
        n = len(s)
        tracker = {}
        best = 0
        last = 0

        for i in range(n):
            if s[i] in tracker and tracker[s[i]] >= last:
                # We only need to remove the previous occurrence from the
                # current window—not discard every other character. Therefore,
                # setting last = i + 1 would be wrong.
                last = tracker[s[i]] + 1

            tracker[s[i]] = i
            # Add one because both endpoints belong to the current window.
            best = max(best, i - last + 1)

        return best
