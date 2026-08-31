"""LeetCode 733: Flood Fill.

Problem: https://leetcode.com/problems/flood-fill/

Time complexity: O(n * m)
Space complexity: O(n * m)
"""

from typing import List


class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
    ) -> List[List[int]]:
        prev_color = image[sr][sc]
        if prev_color == color:
            return image

        unvisited = [[sr, sc]]
        image[sr][sc] = color
        n = len(image)
        m = len(image[0])

        # BFS non-deque implementation.
        head = 0
        while head < len(unvisited):
            # Implement a moving head since popping from the front is costly.
            node = unvisited[head]
            x, y = node[0], node[1]
            head += 1

            if x > 0:
                if image[x - 1][y] == prev_color:
                    unvisited.append([x - 1, y])
                    image[x - 1][y] = color

            if x < n - 1:
                if image[x + 1][y] == prev_color:
                    unvisited.append([x + 1, y])
                    image[x + 1][y] = color

            if y > 0:
                if image[x][y - 1] == prev_color:
                    unvisited.append([x, y - 1])
                    image[x][y - 1] = color

            if y < m - 1:
                if image[x][y + 1] == prev_color:
                    unvisited.append([x, y + 1])
                    image[x][y + 1] = color

        return image
