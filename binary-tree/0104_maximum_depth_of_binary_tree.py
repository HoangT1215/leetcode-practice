"""LeetCode 104: Maximum Depth of Binary Tree.

Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Time complexity: O(n)
Auxiliary space complexity: O(h), where h is the tree height

LeetCode provides the TreeNode class; do not redefine it in the submission.
"""

from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right),
        )
