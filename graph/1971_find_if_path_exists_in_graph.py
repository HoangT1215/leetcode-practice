"""LeetCode 1971: Find if Path Exists in Graph.

Problem: https://leetcode.com/problems/find-if-path-exists-in-graph/

Time complexity: O(V + E)
Space complexity: O(V + E)
"""

from collections import deque  # queue for BFS


class Solution:
    def validPath(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        destination: int,
    ) -> bool:
        graph = [[] for _ in range(n)]

        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)

        visited = {source}  # tracking visited vertices
        # stack = [source]  # tracking vertices that need to be explored
        queue = deque([source])  # tracking vertices using queue

        # while stack:  # DFS
        while queue:  # BFS
            # --- DFS
            # vertex = stack.pop()  # popping vertices gives a stopping condition
            # If you instead removed from the front of a queue, it would be BFS.
            # For merely determining whether a path exists, either method works.

            # --- BFS
            vertex = queue.popleft()

            if vertex == destination:
                return True

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # stack.append(neighbor)  # DFS
                    queue.append(neighbor)  # BFS

        return False
