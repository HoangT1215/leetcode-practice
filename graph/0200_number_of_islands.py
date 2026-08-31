"""LeetCode 200: Number of Islands.

Problem: https://leetcode.com/problems/number-of-islands/

Time complexity: O(rows * cols)
Space complexity: O(rows * cols)
"""

from typing import List


class Solution:
    def floodfill(
        self, grid: List[List[str]], x: int, y: int
    ) -> List[List[str]]:
        n, m = len(grid), len(grid[0])
        unvisited = [[x, y]]
        head = 0

        # Mark a cell when it enters the queue so it cannot be added twice.
        grid[x][y] = "0"

        # BFS with a moving head. Popping index 0 from a list would cost O(k)
        # because Python would need to shift the remaining k elements.
        while head < len(unvisited):
            node = unvisited[head]
            x, y = node[0], node[1]
            head += 1

            if x > 0:
                if grid[x - 1][y] == "1":
                    unvisited.append([x - 1, y])
                    grid[x - 1][y] = "0"

            if x < n - 1:
                if grid[x + 1][y] == "1":
                    unvisited.append([x + 1, y])
                    grid[x + 1][y] = "0"

            if y > 0:
                if grid[x][y - 1] == "1":
                    unvisited.append([x, y - 1])
                    grid[x][y - 1] = "0"

            if y < m - 1:
                if grid[x][y + 1] == "1":
                    unvisited.append([x, y + 1])
                    grid[x][y + 1] = "0"

        return grid

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)  # rows
        n = len(grid[0])  # columns
        islands = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    # Discovering unvisited land means we found a new island.
                    # Flood fill then marks the entire island as visited.
                    islands += 1
                    grid = self.floodfill(grid, x, y)

        return islands
