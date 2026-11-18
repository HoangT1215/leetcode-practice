"""LeetCode 347: Top K Frequent Elements.

Problem: https://leetcode.com/problems/top-k-frequent-elements/

Time complexity: O(n), expected with hash-map counting.
Auxiliary space complexity: O(n).
"""

from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        counts = Counter(nums)

        # Frequencies range from 1 to len(nums).
        buckets = [[] for _ in range(n + 1)]

        # building bucket
        for number, frequency in counts.items():
            buckets[frequency].append(number)

        result = []

        # Visit the most frequent numbers first.
        i = 0
        for frequency in range(len(nums), 0, -1):
            for number in buckets[frequency]:
                result.append(number)
                i += 1

                if i == k:
                    return result

        return result
