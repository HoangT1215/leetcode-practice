"""LeetCode 2497: Maximum Star Sum of a Graph.

Problem: https://leetcode.com/problems/maximum-star-sum-of-a-graph/

Time complexity: O(E + sum(deg(v) log deg(v)))
Space complexity: O(V + E)
"""

from typing import List


class Solution:
    def maxStarSum(
        self, vals: List[int], edges: List[List[int]], k: int
    ) -> int:
        best = min(vals)
        n = len(vals)
        adj_list = []

        for _ in range(n):
            adj_list.append([])

        for edge in edges:
            i, j = edge[0], edge[1]
            adj_list[i].append(j)
            adj_list[j].append(i)

        for i in range(n):
            val_list = []
            for ind in adj_list[i]:
                val_list.append(vals[ind])

            val_list.sort()
            m = len(val_list)
            j = m - 1
            temp = vals[i]

            while j >= max(0, m - k):
                if val_list[j] >= 0:
                    temp += val_list[j]
                    j -= 1
                else:
                    break

            best = max(best, temp)

        return best
