"""LeetCode 743: Network Delay Time.

Problem: https://leetcode.com/problems/network-delay-time/

Time complexity: O((V + E) log V)
    - Explanation: heap operation is O(log n), while we have to traverse m+n states to check and properly update all vertices
Space complexity: O(V + E)
"""

import heapq
from typing import List


class Solution:
    def networkDelayTime(
        self, times: List[List[int]], n: int, k: int
    ) -> int:
        # graph[u] contains the outgoing (neighbor, weight) pairs from u.
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        # Each entry is (shortest known time, node).
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            # Ignore a stale entry superseded by a shorter path.
            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        answer = max(dist[1:])
        return answer if answer < float("inf") else -1
